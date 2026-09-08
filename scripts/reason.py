"""
Reason step: the final stage. Takes deterministically pre-computed trend
data (from compute_trend.py) plus the original question, and asks the
LLM to state the answer and explain WHY in words. The LLM is explicitly
forbidden from doing its own arithmetic.
"""
import json

from llm_backend import call_llm
from synthesize import extract_json
from compute_trend import compute_trend

REASON_PROMPT_TEMPLATE = """You previously planned and ran GEOS simulations to answer a physics question.

Original question: {question}

Why these runs were needed: {plan_reasoning}

The following trend data was computed with exact arithmetic in Python - every
number below (differences, percent changes, direction) is already correct.
Do NOT recompute, re-derive, or double-check any of these numbers yourself,
and do NOT introduce any new numeric value of your own:

{trend_summary}

CRITICAL RULES:
1. Use ONLY the numbers given above. Do not perform your own subtraction,
   percentage, or other arithmetic - copy the precomputed values verbatim.
2. If a "REQUESTED COMPARISON" block is present above, that is the specific
   pair the question asked about - use its diff/percent-change directly in
   your answer. Do not substitute a different pair's numbers.
3. Your explanation may describe the QUALITATIVE physical mechanism for why
   the trend goes in this direction, but it must be consistent with the
   direction given above - if the data shows the value increasing, your
   mechanism must explain an increase, not a decrease.
4. If your own physics intuition about the mechanism seems to disagree with
   the observed direction, trust the observed direction - state the
   mechanism in whatever way is consistent with it, rather than describing
   the opposite mechanism.

Respond with ONLY a JSON object (no markdown fences, no prose) in exactly this form:
{{
  "answer": "<direct, specific answer to the question, using the precomputed numbers above verbatim>",
  "explanation": "<qualitative physical mechanism for why the results differ in this direction - no new numeric estimates, no arithmetic>",
  "any_health_concerns": "<note any run that did not complete cleanly (timestep cuts, non-convergence) - or 'none' if all runs were clean>"
}}
"""


def reason_over_results(gathered, changed_param=None, primary_pair=None, use_api=True, provider="openai", model=None):
    trend = compute_trend(
        gathered["run_results"], changed_param=changed_param, primary_pair=primary_pair
    )
    prompt = REASON_PROMPT_TEMPLATE.format(
        question=gathered["question"],
        plan_reasoning=gathered["plan_reasoning"],
        trend_summary=trend["summary_text"],
    )
    raw_response = call_llm(prompt, use_api=use_api, provider=provider, model=model)
    parsed = extract_json(raw_response)

    return {
        "question": gathered["question"],
        "answer": parsed.get("answer"),
        "explanation": parsed.get("explanation"),
        "any_health_concerns": parsed.get("any_health_concerns"),
        "trend": trend,
        "grounded_in_results": gathered["run_results"],
        "raw_llm_response": raw_response,
    }
