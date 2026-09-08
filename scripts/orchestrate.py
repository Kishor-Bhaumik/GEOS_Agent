"""
Execute + Gather step: takes a plan (from plan.py) and, for each run,
synthesizes a deck, runs GEOS, and extracts the requested QoI. Purely
mechanical - no LLM judgement happens here, only in plan.py (before) and
reason.py (after).

llm_kwargs is a generic pass-through dict for any provider-specific LLM
call options (max_tokens, enable_thinking, temperature, etc.) so new
options never require editing this file again.

A generic retry loop re-synthesizes with an added warning (not tied to
any specific question's numbers) when a consistency check fails, since
the same class of mistake (editing structural/scheduling elements, or
contradicting the run's own description) can recur across any provider
or question.
"""
import os
import subprocess

from synthesize import synthesize_deck
from eval_runner import ensure_vtk_output, parse_run_log
from gutils import get_qoi_at_x
from consistency_check import check_all

CONSISTENCY_RETRY_WARNING = (
    " IMPORTANT CORRECTION: A previous attempt at this same task made "
    "edits that were flagged as inconsistent: {issue_summary} "
    "Do not edit <Events>, <PeriodicEvent>, or other structural/scheduling "
    "elements (e.g. maxTime, forceDt, timeFrequency, cycleFrequency) unless "
    "the question explicitly asks to change the total simulation duration "
    "or output frequency - reporting a result 'at time T' does NOT mean "
    "editing maxTime to T. Also do not set any attribute to a value that "
    "contradicts what this description says that attribute should be."
)


def _summarize_issues(issues):
    return "; ".join(i["message"] for i in issues)


def execute_run(run, geos_root, geosx_binary, work_dir, qoi_field, qoi_x,
                 use_api=True, provider="openai", model=None,
                 timeout_s=600, **llm_kwargs):
    run_id = run["run_id"]
    run_dir = os.path.join(work_dir, run_id)
    os.makedirs(run_dir, exist_ok=True)

    synth_path = os.path.join(run_dir, "synthesized.xml")
    synth_result = synthesize_deck(
        question=run["description"],
        geos_root=geos_root,
        output_path=synth_path,
        use_api=use_api,
        provider=provider,
        model=model,
        **llm_kwargs,
    )

    if not synth_result["lint_clean"]:
        return {
            "run_id": run_id, "status": "FAIL_LINT",
            "description": run["description"], "synth_result": synth_result,
        }

    consistency_issues = check_all(run["description"], synth_result["edits_applied"])
    if consistency_issues:
        return {
            "run_id": run_id, "status": "FAIL_CONSISTENCY",
            "description": run["description"], "synth_result": synth_result,
            "consistency_issues": consistency_issues,
        }

    vtk_path = os.path.join(run_dir, "deck_vtk.xml")
    ensure_vtk_output(synth_path, vtk_path)

    output_dir = os.path.join(run_dir, "output")
    try:
        proc = subprocess.run(
            [geosx_binary, "-i", vtk_path, "-o", output_dir],
            capture_output=True, text=True, timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        return {
            "run_id": run_id, "status": "FAIL_TIMEOUT",
            "description": run["description"], "synth_result": synth_result,
        }

    log_text = proc.stdout + proc.stderr
    with open(os.path.join(run_dir, "run.log"), "w") as f:
        f.write(log_text)
    health = parse_run_log(log_text)

    if proc.returncode != 0 or not health["reached_end"]:
        return {
            "run_id": run_id, "status": "FAIL_RUN",
            "description": run["description"],
            "synth_result": synth_result, "run_health": health,
        }

    try:
        extracted = get_qoi_at_x(output_dir, qoi_field, qoi_x)
    except Exception as e:
        return {
            "run_id": run_id, "status": "FAIL_EXTRACT",
            "description": run["description"],
            "synth_result": synth_result, "run_health": health,
            "error": str(e),
        }

    return {
        "run_id": run_id,
        "status": "PASS",
        "description": run["description"],
        "anchor_chosen": synth_result["anchor_chosen"],
        "edits_applied": synth_result["edits_applied"],
        "run_health": health,
        "qoi_field": qoi_field,
        "qoi_x": qoi_x,
        "qoi_value": extracted["value"],
    }


def execute_run_with_retry(run, geos_root, geosx_binary, work_dir, qoi_field, qoi_x,
                            use_api=True, provider="openai", model=None,
                            timeout_s=600, max_retries=2, **llm_kwargs):
    current_run = run
    attempts = []
    for attempt in range(max_retries + 1):
        result = execute_run(
            current_run, geos_root, geosx_binary, work_dir, qoi_field, qoi_x,
            use_api=use_api, provider=provider, model=model,
            timeout_s=timeout_s, **llm_kwargs,
        )
        attempts.append({"attempt": attempt, "status": result["status"]})

        if result["status"] != "FAIL_CONSISTENCY":
            result["retry_attempts"] = attempts
            return result

        if attempt < max_retries:
            issue_summary = _summarize_issues(result["consistency_issues"])
            warning = CONSISTENCY_RETRY_WARNING.format(issue_summary=issue_summary)
            current_run = {**current_run, "description": run["description"] + warning}

    result["retry_attempts"] = attempts
    return result


def execute_plan(plan_result, geos_root, geosx_binary, work_dir,
                  qoi_field="pressure", qoi_x=5.0, use_api=True,
                  provider="openai", model=None, max_retries=2, **llm_kwargs):
    results = []
    for run in plan_result["runs"]:
        print(f"Executing run: {run['run_id']} ...", flush=True)
        r = execute_run_with_retry(
            run, geos_root, geosx_binary, work_dir, qoi_field, qoi_x,
            use_api=use_api, provider=provider, model=model,
            max_retries=max_retries, **llm_kwargs,
        )
        results.append(r)
        suffix = f", {qoi_field}={r.get('qoi_value')}" if r["status"] == "PASS" else ""
        n_attempts = len(r.get("retry_attempts", []))
        print(f"  -> {r['status']}{suffix} (attempts: {n_attempts})")

    return {
        "question": plan_result["question"],
        "plan_reasoning": plan_result["reasoning"],
        "run_results": results,
    }
