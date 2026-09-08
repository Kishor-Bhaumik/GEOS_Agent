"""
Probe step: given the parameter that changed between base and modified
runs (from diff_runs.py), ask the LLM to propose a third value for that
SAME parameter that will help confirm the direction of the trend - then
synthesize and run that probe deck the same way as any other run.
"""
from llm_backend import call_llm
from synthesize import extract_json

PROBE_PROMPT_TEMPLATE = """A simulation comparison changed this parameter between two runs:

Attribute: {attr}
XPath: {xpath}
Base case value: {value_a}
Modified case value: {value_b}

To verify the direction of the trend this parameter change causes (rather
than relying on physics intuition alone), propose ONE additional "probe"
value for this SAME parameter - a third data point that, together with
the two values above, will make the trend direction unambiguous from the
observed numbers alone (e.g. a value on the opposite side of the base
case, or a value that extends the same trend further).

Respond with ONLY a JSON object (no markdown fences, no prose):
{{
  "probe_value": "<the new value to use for this attribute, as a string>",
  "reasoning": "<one sentence on why this probe value will help disambiguate the trend>"
}}
"""


def plan_probe(changed_param, use_api=True):
    prompt = PROBE_PROMPT_TEMPLATE.format(
        attr=changed_param["attr"],
        xpath=changed_param["xpath"],
        value_a=changed_param["value_in_run_a"],
        value_b=changed_param["value_in_run_b"],
    )
    raw_response = call_llm(prompt, use_api=use_api)
    parsed = extract_json(raw_response)
    return {
        "xpath": changed_param["xpath"],
        "attr": changed_param["attr"],
        "probe_value": parsed.get("probe_value"),
        "reasoning": parsed.get("reasoning"),
    }


def build_probe_run_description(base_run_description, probe):
    return (
        f"{base_run_description} "
        f"EXCEPT: set the attribute '{probe['attr']}' at xpath '{probe['xpath']}' "
        f"to {probe['probe_value']} instead of its base-case value."
    )
