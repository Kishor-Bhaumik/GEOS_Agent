"""
Deterministic diff between two runs' edits_applied lists. Purely
mechanical - finds which (xpath, attr) actually changed value between
two runs, with no physics knowledge. Works for any GEOS physics family
because it only compares XML attribute values, never interprets them.
"""


def find_changed_parameter(run_a, run_b):
    edits_a = {(e["xpath"], e["attr"]): e["new_value"] for e in run_a.get("edits_applied", [])}
    edits_b = {(e["xpath"], e["attr"]): e["new_value"] for e in run_b.get("edits_applied", [])}

    all_keys = set(edits_a.keys()) | set(edits_b.keys())
    changed = []
    for key in all_keys:
        xpath, attr = key
        val_a = edits_a.get(key)
        val_b = edits_b.get(key)
        if val_a != val_b:
            changed.append({
                "xpath": xpath,
                "attr": attr,
                "value_in_run_a": val_a,
                "value_in_run_b": val_b,
            })
    return changed
