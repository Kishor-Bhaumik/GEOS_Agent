"""
Plan step: given a (possibly counterfactual/what-if) question, ask the LLM
to decide how many GEOS simulation runs are needed and what each run
should represent - BEFORE any deck synthesis or execution happens.
"""
from llm_backend import call_llm
from synthesize import extract_json

PLAN_PROMPT_TEMPLATE = """You are planning what GEOS simulations are needed to answer a physics question.

Question: {question}

Budget: you may plan AT MOST {max_runs} total simulation runs. Use fewer
if the question doesn't need that many - the budget is a ceiling, not a
target. If answering thoroughly (e.g. isolating multiple changed
parameters one at a time) would require more than {max_runs} runs,
prioritize the run(s) most likely to answer the question and explain
your prioritization in "reasoning".

Some questions can be answered with a single simulation. Others are
counterfactual / "what if" questions that require comparing multiple
simulation runs (e.g. a base case and one or more modified cases) to
answer how a change in some parameter affects the result.

Respond with ONLY a JSON object (no markdown fences, no prose) in exactly this form:
{{
  "reasoning": "<one or two sentences on why this many runs are needed, and how you prioritized if the budget was limiting>",
  "runs": [
    {{"run_id": "<short id>", "description": "<precise, SELF-CONTAINED natural language description of this run>"}}
  ]
}}

Rules:
- If the question can be answered with one simulation, return exactly one run.
- If the question asks "what if X changes compared to the base/current case", return at least two runs: one baseline run and one run per modified scenario.
- Never return more than {max_runs} runs.
- CRITICAL: each run's description must be a COMPLETE, ABSOLUTE, standalone specification of that scenario - restate every relevant physical parameter (geometry, materials, boundary conditions) explicitly, every time. NEVER write relative phrases like "base case, no changes" or "same as before" - each run is synthesized independently by someone with NO memory of the other runs or of this question, so a relative description gives them nothing to build from.
- Extract every specific number given in the question (dimensions, compressibility values, pressure BCs, etc.) and repeat the full relevant set of them in EVERY run's description, changing only the parameter(s) the question asks about.
"""


def build_plan_prompt(question, max_runs=6):
    return PLAN_PROMPT_TEMPLATE.format(question=question, max_runs=max_runs)


def make_plan(question, use_api=True, max_runs=6, **kwargs):
    prompt = build_plan_prompt(question, max_runs=max_runs)
    raw_response = call_llm(prompt, use_api=use_api, **kwargs)
    parsed = extract_json(raw_response)
    runs = parsed.get("runs", [])

    if len(runs) > max_runs:
        runs = runs[:max_runs]

    return {
        "question": question,
        "reasoning": parsed.get("reasoning"),
        "runs": runs,
        "raw_llm_response": raw_response,
    }
