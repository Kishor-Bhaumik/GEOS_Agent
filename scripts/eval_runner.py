"""
Eval runner for the GEOS agent pipeline.

For each case: lint -> (if broken) repair -> run geosx -> parse health ->
extract QoI -> compare with tolerance -> report pass/fail.
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from semantic_linter import lint_deck
from gutils import get_qoi_at_x
from repair import repair_and_verify

QOI_KEY_PATTERN = re.compile(r'^(?P<field>[a-zA-Z]+)_at_x(?P<x>[\d.]+)m')


def parse_run_log(log_text):
    health = {
        "timesteps": None,
        "timestep_cuts": None,
        "nonlinear_iters": None,
        "reached_end": False,
    }
    m = re.search(r'Time steps\s*\|\s*(\d+)', log_text)
    if m:
        health["timesteps"] = int(m.group(1))
    m = re.search(r'Time step cuts\s*\|\s*(\d+)', log_text)
    if m:
        health["timestep_cuts"] = int(m.group(1))
    m = re.search(r'Successful nonlinear iterations\s*\|\s*(\d+)', log_text)
    if m:
        health["nonlinear_iters"] = int(m.group(1))
    health["reached_end"] = (
        "End of TIMESTEP" in log_text or "Cleaning up events" in log_text
    )
    return health


def ensure_vtk_output(deck_path, tmp_path):
    with open(deck_path) as f:
        content = f.read()
    new_content = re.sub(r'<Silo(\s+name="[^"]+"\s*/>)', r'<VTK\1', content)
    with open(tmp_path, "w") as f:
        f.write(new_content)
    return new_content != content


def run_case(case, geos_root, geosx_binary, work_dir, timeout_s=600):
    deck_abs = os.path.join(geos_root, case["deck_path"])
    result = {"question_id": case["question_id"], "status": None, "details": {}}

    case_dir = os.path.join(work_dir, case["question_id"])
    os.makedirs(case_dir, exist_ok=True)

    # 1. Lint before doing anything else - cheap, catches broken decks fast.
    lint_result = lint_deck(deck_abs)
    if lint_result.has_errors:
        # Attempt one deterministic repair pass (C1/C2-class: dangling name
        # references only). This never touches physics/numerics fields -
        # see repair.py's mutability rule.
        repaired_path = os.path.join(case_dir, "repaired_deck.xml")
        repair_report = repair_and_verify(deck_abs, repaired_path)
        result["details"]["lint"] = lint_result.report()
        result["details"]["repair_attempt"] = repair_report

        if repair_report["status"] != "REPAIRED_CLEAN":
            result["status"] = "FAIL_LINT"
            return result

        # Repair succeeded - continue the pipeline using the repaired deck.
        deck_abs = repaired_path
    else:
        result["details"]["lint"] = lint_result.report()

    # 2. Prepare a run-local copy of the deck with VTK output guaranteed.
    tmp_deck = os.path.join(case_dir, "deck.xml")
    swapped = ensure_vtk_output(deck_abs, tmp_deck)
    result["details"]["silo_to_vtk_swap_applied"] = swapped

    # 3. Run geosx.
    output_dir = os.path.join(case_dir, "output")
    try:
        proc = subprocess.run(
            [geosx_binary, "-i", tmp_deck, "-o", output_dir],
            capture_output=True, text=True, timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "FAIL_TIMEOUT"
        return result

    log_text = proc.stdout + proc.stderr
    with open(os.path.join(case_dir, "run.log"), "w") as f:
        f.write(log_text)

    health = parse_run_log(log_text)
    result["details"]["run_health"] = health

    if proc.returncode != 0 or not health["reached_end"]:
        result["status"] = "FAIL_RUN"
        result["details"]["returncode"] = proc.returncode
        return result

    if health["timestep_cuts"] and health["timestep_cuts"] > 0:
        result["status"] = "FAIL_HEALTH"
        result["details"]["reason"] = f"{health['timestep_cuts']} timestep cuts"
        return result

    # 4. Extract each QoI and compare against expected_qoi within tolerance.
    all_pass = True
    qoi_results = {}
    for qoi_key, expected_value in case["expected_qoi"].items():
        match = QOI_KEY_PATTERN.match(qoi_key)
        if not match:
            qoi_results[qoi_key] = {
                "status": "SKIP",
                "reason": "could not parse field/x from qoi_key",
            }
            continue
        field = match.group("field")
        x = float(match.group("x"))
        unit_suffix = qoi_key.split("_")[-1]
        tol_key = f"tolerance_{unit_suffix}"
        tolerance = case.get(tol_key)
        if tolerance is None:
            tolerance = case.get("tolerance", 1e-3)

        try:
            extracted = get_qoi_at_x(output_dir, field, x)
            actual_value = extracted["value"]
            diff = abs(actual_value - expected_value)
            passed = diff <= tolerance
            qoi_results[qoi_key] = {
                "expected": expected_value,
                "actual": actual_value,
                "diff": diff,
                "tolerance": tolerance,
                "status": "PASS" if passed else "FAIL",
            }
            if not passed:
                all_pass = False
        except Exception as e:
            qoi_results[qoi_key] = {"status": "ERROR", "error": str(e)}
            all_pass = False

    result["details"]["qoi"] = qoi_results
    result["status"] = "PASS" if all_pass else "FAIL_QOI"
    return result


def main():
    parser = argparse.ArgumentParser(description="Run the GEOS agent eval set.")
    parser.add_argument("--eval-set", required=True, help="Path to eval_set.jsonl")
    parser.add_argument("--geos-root", required=True, help="Path to the GEOS repo root")
    parser.add_argument("--geosx-binary", required=True, help="Path to the geosx binary")
    parser.add_argument("--work-dir", default="/tmp/geosagent_eval_runs")
    parser.add_argument("--only", default=None, help="Run only this question_id")
    args = parser.parse_args()

    cases = []
    with open(args.eval_set) as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))

    if args.only:
        cases = [c for c in cases if c["question_id"] == args.only]

    os.makedirs(args.work_dir, exist_ok=True)
    results = []
    for case in cases:
        print(f"Running {case['question_id']} ...", flush=True)
        r = run_case(case, args.geos_root, args.geosx_binary, args.work_dir)
        results.append(r)
        print(f"  -> {r['status']}")

    print("\n=== Summary ===")
    n_pass = sum(1 for r in results if r["status"] == "PASS")
    print(f"{n_pass}/{len(results)} passed")
    for r in results:
        print(f"  {r['question_id']}: {r['status']}")

    summary_path = os.path.join(args.work_dir, "results.json")
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull details written to {summary_path}")


if __name__ == "__main__":
    main()
