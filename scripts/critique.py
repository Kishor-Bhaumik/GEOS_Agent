"""
Self-critique step: after reason.py produces an answer + explanation,
ask the model to critique its OWN explanation and decide whether
additional simulations would help verify it - and if so, propose them
within a budget.

To reduce token cost, known governing-physics relations are given
directly in the prompt so the model doesn't need to re-derive them from
scratch - it should use them, not derive them.
"""
from llm_backend import call_llm
from synthesize import extract_json

CRITIQUE_PROMPT_TEMPLATE = """You previously answered this question based on simulation results:

Question: {question}

Your answer: {answer}
Your explanation: {explanation}

Trend data your answer was based on:
{trend_summary}

Known physics relation (use this directly - do NOT re-derive it from first
principles, and do not write out a full derivation):
For 1D single-phase pressure diffusion, D = k / (mu * phi * c), where c is
compressibility. Lower c gives higher D (faster pressure propagation).
The steady-state pressure profile depends only on permeability/geometry,
not on compressibility - compressibility only affects transient behavior.

Using that relation directly, briefly critique your OWN explanation (a few
sentences, not a derivation). Is your explanation actually consistent with
that relation, or is it an unrelated analogy (e.g. mechanical "stiffness")
that happens to match the observed direction without being the real cause?

Consider: is there a DIFFERENT simulation you could run whose result would
be different depending on whether your explanation is right or wrong (a
genuinely discriminating test - one where a wrong explanation and the
correct mechanism predict OPPOSITE results, not just another data point
in the same direction)?

You have a budget of at most {max_probes} additional simulation runs.

Respond with ONLY a JSON object (no markdown fences, no prose, no derivation):
{{
  "needs_verification": <true or false>,
  "confidence_in_explanation": "<low, medium, or high, with a one-sentence reason>",
  "proposed_probes": [
    {{"description": "<a full, self-contained, absolute description of this probe run, following the same rules as base/modified run descriptions - complete parameter set, not relative>", "what_it_would_show": "<what result would confirm vs refute your explanation - state what EACH competing explanation predicts if they differ>"}}
  ]
}}

If needs_verification is false, proposed_probes should be an empty list.
Never propose more than {max_probes} probes. Keep all text fields brief.
"""


def critique_explanation(question, answer, explanation, trend_summary,
                          max_probes=3, use_api=True, provider="deepseek",
                          model=None, max_tokens=6000):
    prompt = CRITIQUE_PROMPT_TEMPLATE.format(
        question=question,
        answer=answer,
        explanation=explanation,
        trend_summary=trend_summary,
        max_probes=max_probes,
    )
    raw_response = call_llm(
        prompt, use_api=use_api, provider=provider, model=model, max_tokens=max_tokens
    )
    parsed = extract_json(raw_response)

    probes = parsed.get("proposed_probes", [])
    if len(probes) > max_probes:
        probes = probes[:max_probes]

    return {
        "needs_verification": parsed.get("needs_verification", False),
        "confidence_in_explanation": parsed.get("confidence_in_explanation"),
        "proposed_probes": probes,
        "raw_llm_response": raw_response,
    }
