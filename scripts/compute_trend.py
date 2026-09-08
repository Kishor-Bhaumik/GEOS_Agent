"""
Deterministic trend computation across multiple runs (base + modified +
any probes). This does ALL the arithmetic - diffs, percent changes,
monotonicity - in plain Python, because LLMs are unreliable at exact
multi-digit arithmetic. reason.py should never ask the LLM to subtract
or compare numbers; it should only ever be given the output of this
module to restate in words.
"""


def _extract_param_value(run, xpath, attr):
    for e in run.get("edits_applied", []):
        if e["xpath"] == xpath and e["attr"] == attr:
            try:
                return float(e["new_value"])
            except (TypeError, ValueError):
                return None
    return None


def compute_trend(run_results, changed_param=None, primary_pair=None):
    passed = [r for r in run_results if r.get("status") == "PASS"]
    if len(passed) < 2:
        return {
            "n_points": len(passed),
            "pairs": [],
            "monotonic": None,
            "summary_text": (
                f"Only {len(passed)} successful run(s) available - "
                f"no trend can be computed."
            ),
        }

    by_id = {r["run_id"]: r for r in passed}

    points = []
    for r in passed:
        param_value = None
        if changed_param:
            param_value = _extract_param_value(
                r, changed_param["xpath"], changed_param["attr"]
            )
        points.append({
            "run_id": r["run_id"],
            "param_value": param_value,
            "qoi_value": r["qoi_value"],
        })

    if changed_param and all(p["param_value"] is not None for p in points):
        points.sort(key=lambda p: p["param_value"])

    pairs = []
    diffs = []
    for i in range(len(points) - 1):
        a, b = points[i], points[i + 1]
        diff = b["qoi_value"] - a["qoi_value"]
        pct = (diff / a["qoi_value"] * 100) if a["qoi_value"] != 0 else None
        diffs.append(diff)
        pairs.append({
            "from_run": a["run_id"], "to_run": b["run_id"],
            "from_param_value": a["param_value"], "to_param_value": b["param_value"],
            "from_qoi": a["qoi_value"], "to_qoi": b["qoi_value"],
            "diff": diff, "percent_change": pct,
        })

    signs = set(1 if d > 0 else (-1 if d < 0 else 0) for d in diffs)
    if len(signs) == 1 and 0 not in signs:
        monotonic = "increasing" if signs == {1} else "decreasing"
    else:
        monotonic = "non-monotonic"

    lines = []

    primary_block = None
    if primary_pair and primary_pair[0] in by_id and primary_pair[1] in by_id:
        run_a = by_id[primary_pair[0]]
        run_b = by_id[primary_pair[1]]
        p_diff = run_b["qoi_value"] - run_a["qoi_value"]
        p_pct = (p_diff / run_a["qoi_value"] * 100) if run_a["qoi_value"] != 0 else None
        pct_str = f" ({p_pct:.2f}%)" if p_pct is not None else ""
        primary_block = {
            "from_run": primary_pair[0], "to_run": primary_pair[1],
            "from_qoi": run_a["qoi_value"], "to_qoi": run_b["qoi_value"],
            "diff": p_diff, "percent_change": p_pct,
        }
        lines.append(
            f"REQUESTED COMPARISON (this is the pair the question asked about "
            f"- use THIS diff, not any other pair, when answering the question directly):"
        )
        lines.append(f"  {primary_pair[0]}: qoi={run_a['qoi_value']}")
        lines.append(f"  {primary_pair[1]}: qoi={run_b['qoi_value']}")
        lines.append(f"  Change from {primary_pair[0]} to {primary_pair[1]}: {p_diff:.6g}{pct_str}")
        lines.append("")

    lines.append(f"All data points ({len(points)} total), sorted by parameter value:")
    for p in points:
        param_str = f"param={p['param_value']}, " if p["param_value"] is not None else ""
        lines.append(f"  - {p['run_id']}: {param_str}qoi={p['qoi_value']}")
    lines.append(f"Overall trend across all points: {monotonic}")
    lines.append("Step-by-step changes between adjacent sorted points (for trend confirmation only):")
    for pair in pairs:
        pct_str = f" ({pair['percent_change']:.2f}%)" if pair["percent_change"] is not None else ""
        lines.append(
            f"  - {pair['from_run']} -> {pair['to_run']}: "
            f"change = {pair['diff']:.6g}{pct_str}"
        )

    return {
        "n_points": len(points),
        "points": points,
        "pairs": pairs,
        "primary_comparison": primary_block,
        "monotonic": monotonic,
        "summary_text": "\n".join(lines),
    }
