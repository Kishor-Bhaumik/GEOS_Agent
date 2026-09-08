"""
Generic edit-consistency check: catches the class of bug where an LLM's
proposed edits contradict its OWN run description, or touch high-risk
structural elements (Events/timing) that are usually not what the
question intended.
"""
import re

SYNONYM_GROUPS = {
    "initial": ["initial", "initially"],
    "source": ["source", "inject", "injected"],
    "sink": ["sink", "held at", "boundary", "outlet"],
}

NUMBER_PATTERN = re.compile(r'-?\d+\.?\d*(?:[eE][-+]?\d+)?')
COORDINATE_PATTERN = re.compile(r'x\s*=\s*-?\d+\.?\d*\s*m?', re.IGNORECASE)

UNIT_MULTIPLIERS = {
    "mpa": 1e6, "kpa": 1e3, "pa": 1.0,
}


def _find_keyword_numbers(description, phrases, window=60, unit_hint=None):
    scrubbed = COORDINATE_PATTERN.sub("x=<coord>", description)

    found = []
    for phrase in phrases:
        for m in re.finditer(re.escape(phrase), scrubbed, re.IGNORECASE):
            snippet = scrubbed[m.end(): m.end() + window]
            num_match = NUMBER_PATTERN.search(snippet)
            if not num_match:
                continue
            value = float(num_match.group(0))

            if unit_hint == "pressure":
                suffix_match = re.match(
                    r'\s*([kKmM]?[pP][aA])', snippet[num_match.end():num_match.end() + 5]
                )
                if not suffix_match:
                    continue
                unit = suffix_match.group(1).lower()
                value *= UNIT_MULTIPLIERS.get(unit, 1.0)
            elif unit_hint == "temperature":
                if not re.match(r'\s*K\b', snippet[num_match.end():num_match.end() + 3]):
                    continue
            found.append(value)
    return found


def _element_name_from_xpath(xpath):
    m = re.search(r"@name='([^']+)'", xpath)
    return m.group(1) if m else ""


def check_edit_consistency(description, edits_applied, tolerance=1e-6):
    issues = []
    for edit in edits_applied:
        if edit.get("old_value") == edit.get("new_value"):
            continue

        try:
            new_val = float(edit["new_value"])
        except (TypeError, ValueError):
            continue

        element_name = _element_name_from_xpath(edit["xpath"]).lower()
        if not element_name:
            continue

        for group_key, phrases in SYNONYM_GROUPS.items():
            if group_key not in element_name:
                continue
            unit_hint = "pressure" if "pressure" in element_name else (
                "temperature" if "temperature" in element_name else None
            )
            expected_numbers = _find_keyword_numbers(description, phrases, unit_hint=unit_hint)
            if not expected_numbers:
                continue
            if not any(abs(new_val - n) <= tolerance * max(1, abs(n)) for n in expected_numbers):
                issues.append({
                    "xpath": edit["xpath"],
                    "attr": edit["attr"],
                    "element_name": element_name,
                    "matched_keyword_group": group_key,
                    "new_value": new_val,
                    "expected_from_description": expected_numbers,
                    "message": (
                        f"Element '{element_name}' (matches keyword group "
                        f"'{group_key}') was set to {new_val}, but the run's "
                        f"own description associates '{group_key}'-related "
                        f"phrases with {expected_numbers} instead."
                    ),
                })
    return issues


RISKY_STRUCTURAL_PATHS = ["events", "periodicevent"]


def flag_risky_structural_edits(edits_applied):
    issues = []
    for edit in edits_applied:
        if edit.get("old_value") == edit.get("new_value"):
            continue
        xpath_lower = edit["xpath"].lower()
        if any(p in xpath_lower for p in RISKY_STRUCTURAL_PATHS):
            issues.append({
                "xpath": edit["xpath"],
                "attr": edit["attr"],
                "old_value": edit["old_value"],
                "new_value": edit["new_value"],
                "message": (
                    f"Edit touches a structural/scheduling element "
                    f"({edit['xpath']}), changing '{edit['attr']}' from "
                    f"{edit['old_value']} to {edit['new_value']}. This "
                    f"controls simulation duration/timing, not a physical "
                    f"field value - verify this was actually intended by "
                    f"the question, rather than a misreading of an "
                    f"'at time T' observation request as a duration change."
                ),
            })
    return issues


def check_all(description, edits_applied):
    """Convenience wrapper running both checks."""
    return check_edit_consistency(description, edits_applied) + \
        flag_risky_structural_edits(edits_applied)
