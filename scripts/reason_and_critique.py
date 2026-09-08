"""
Combined Reason + Self-Critique + Probe-proposal step, using dynamically
retrieved domain knowledge (from domain_knowledge.py) instead of a
hand-written, physics-family-specific formula. This scales to any GEOS
solver without us writing new physics facts per family.
"""
from llm_backend import call_llm
from synthesize import extract_json
from compute_trend import compute_trend
from domain_knowledge import get_domain_knowledge

COMBINED_PROMPT_TEMPLATE = """You are answering a physics question using GEOS simulation results.

Original question: {question}

Why these runs were needed: {plan_reasoning}

The following trend data was computed with exact arithmetic in Python - every
number below is already correct. Do NOT recompute or introduce new numeric
values yourself - use these verbatim.

{trend_summary}

{domain_knowledge_block}

Do all of the following in one pass:
1. Answer the question using the precomputed numbers above (if a "REQUESTED
   COMPARISON" block is present, use that pair's diff/percent-change directly).
2. Give a qualitative physical mechanism explanation, grounded in the
   governing equation above (if provided) rather than an unrelated analogy,
   and consistent with the observed direction.
3. Critique your OWN explanation from step 2: is it really the correct
   mechanism, or an oversimplified/wrong analogy that happens to match the
   observed direction? Be brief.
4. If you have any doubt, propose at most {max_probes} additional simulation
   run(s) that would be GENUINELY DISCRIMINATING - i.e. a wrong explanation
   and the correct mechanism would predict OPPOSITE results, not just
   another data point in the same direction. Each probe description must be
   a full, self-contained, absolute specification (complete parameter set,
   not relative to "the base case").

Respond with ONLY a JSON object (no markdown fences, no prose, no derivation
outside the fields below):
{{
  "answer": "<direct answer using the precomputed numbers verbatim>",
  "explanation": "<qualitative mechanism, no new arithmetic>",
  "confidence_in_explanation": "<low, medium, or high, with a one-sentence reason>",
  "needs_verification": <true or false>,
  "proposed_probes": [
    {{"description": "<full self-contained probe description>", "what_it_would_show": "<what each competing explanation predicts, if they differ>"}}
  ],
  "any_health_concerns": "<note any run that did not complete cleanly, or 'none'>"
}}

If needs_verification is false, proposed_probes should be an empty list.
"""


def _format_domain_knowledge_block(dk):
    if dk is None:
        return (
            "No solver documentation was found for this deck - reason from "
            "general physics principles, and flag lower confidence accordingly."
        )
    return (
        f"Governing equation documentation for solver '{dk['solver_name']}' "
        f"(retrieved from GEOS's own docs, use directly - do not re-derive):\n"
        f"{dk['excerpt']}"
    )


def reason_and_critique(gathered, geos_root, anchor_deck_relpath,
                         changed_param=None, primary_pair=None,
                         max_probes=2, use_api=True, provider="deepseek",
                         model=None, **llm_kwargs):
    trend = compute_trend(
        gathered["run_results"], changed_param=changed_param, primary_pair=primary_pair
    )

    import os
    deck_abs_path = os.path.join(geos_root, anchor_deck_relpath)
    dk = get_domain_knowledge(deck_abs_path, geos_root)
    domain_knowledge_block = _format_domain_knowledge_block(dk)

    prompt = COMBINED_PROMPT_TEMPLATE.format(
        question=gathered["question"],
        plan_reasoning=gathered["plan_reasoning"],
        trend_summary=trend["summary_text"],
        domain_knowledge_block=domain_knowledge_block,
        max_probes=max_probes,
    )
    llm_kwargs.setdefault("max_tokens", 8000)
    raw_response = call_llm(
        prompt, use_api=use_api, provider=provider, model=model, **llm_kwargs
    )
    parsed = extract_json(raw_response)

    probes = parsed.get("proposed_probes", [])
    if len(probes) > max_probes:
        probes = probes[:max_probes]

    return {
        "question": gathered["question"],
        "answer": parsed.get("answer"),
        "explanation": parsed.get("explanation"),
        "confidence_in_explanation": parsed.get("confidence_in_explanation"),
        "needs_verification": parsed.get("needs_verification", False),
        "proposed_probes": probes,
        "any_health_concerns": parsed.get("any_health_concerns"),
        "domain_knowledge_used": dk,
        "trend": trend,
        "grounded_in_results": gathered["run_results"],
        "raw_llm_response": raw_response,
    }
