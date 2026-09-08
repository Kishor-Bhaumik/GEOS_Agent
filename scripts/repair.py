"""
Deterministic repair for reference-integrity errors (semantic_linter's
E_REGION_REF, E_DISCRETIZATION_REF, E_MATERIAL_REF, E_EVENT_TARGET_REF).

This is C1/C2-class repair in the taxonomy: schema/reference errors that
have a single deterministic fix (the name is a typo of something that
already exists in the deck) and require no LLM judgement call.

Mutability rule: this repair ONLY ever rewrites a dangling name to match
an existing declared name in the SAME deck. It never invents a new value,
never touches numeric/physics fields, and never edits anything the linter
did not flag. If no confident nearest-match exists, it refuses and leaves
the file untouched - ambiguity here should escalate, not guess.
"""
import difflib
import re

from semantic_linter import lint_deck

REPAIRABLE_CODES = {
    "E_REGION_REF", "E_DISCRETIZATION_REF", "E_MATERIAL_REF", "E_EVENT_TARGET_REF",
}


def propose_repairs(lint_result, cutoff=0.6):
    proposals = []
    for issue in lint_result.issues:
        if issue.code not in REPAIRABLE_CODES:
            continue
        matches = difflib.get_close_matches(
            issue.bad_value, issue.valid_candidates, n=1, cutoff=cutoff
        )
        proposals.append({
            "code": issue.code,
            "bad_value": issue.bad_value,
            "suggested_value": matches[0] if matches else None,
            "candidates_considered": issue.valid_candidates,
        })
    return proposals


def apply_repairs(xml_path, proposals, output_path):
    with open(xml_path) as f:
        content = f.read()

    applied = []
    skipped = []
    for p in proposals:
        if p["suggested_value"] is None:
            skipped.append(p)
            continue
        pattern = re.compile(r'\b' + re.escape(p["bad_value"]) + r'\b')
        n_matches = len(pattern.findall(content))
        if n_matches == 0:
            skipped.append({**p, "reason": "bad_value not found as whole word in file"})
            continue
        content = pattern.sub(p["suggested_value"], content)
        applied.append({**p, "n_occurrences_replaced": n_matches})

    with open(output_path, "w") as f:
        f.write(content)

    return {"applied": applied, "skipped": skipped}


def repair_and_verify(xml_path, output_path, cutoff=0.6):
    lint_before = lint_deck(xml_path)
    if not lint_before.has_errors:
        return {"status": "NO_REPAIR_NEEDED", "lint_before": lint_before.report()}

    proposals = propose_repairs(lint_before, cutoff=cutoff)
    apply_result = apply_repairs(xml_path, proposals, output_path)

    lint_after = lint_deck(output_path)
    status = "REPAIRED_CLEAN" if not lint_after.has_errors else "REPAIRED_PARTIAL"
    if not apply_result["applied"]:
        status = "REPAIR_FAILED_NO_CONFIDENT_MATCH"

    return {
        "status": status,
        "lint_before": lint_before.report(),
        "applied": apply_result["applied"],
        "skipped": apply_result["skipped"],
        "lint_after": lint_after.report(),
    }


if __name__ == "__main__":
    import sys
    import json
    result = repair_and_verify(sys.argv[1], sys.argv[2])
    print(json.dumps(result, indent=2))
