"""
NL -> deck synthesis. The LLM never writes XML directly; it picks an
anchor deck and proposes structured attribute edits, which deterministic
code applies.

Key fix: the LLM must SEE the actual anchor deck content (not just a
one-line description) or it hallucinates generic simulator element/
attribute names that don't exist in GEOS's real schema.
"""
import json
import os
import re
import xml.etree.ElementTree as ET

from anchor_index import ANCHOR_DECKS, get_anchor_by_filename
from llm_backend import call_llm
from semantic_linter import lint_deck

PROMPT_TEMPLATE = """You are selecting and editing a GEOS simulation input deck to answer a physics question.

Below are the full contents of the available anchor decks. Pick the ONE
that is the closest physical match, using ONLY element names, attribute
names, and structure that you see in these actual files - never invent
or assume names from other simulators.

{anchor_contents}

Question: {question}

Respond with ONLY a JSON object (no markdown fences, no prose) in exactly this form:
{{
  "anchor": "<one of the filenames above>",
  "reasoning": "<one sentence on why this anchor and what needs to change>",
  "edits": [
    {{"op": "set_attribute", "xpath": "<ElementTree find() xpath into the anchor deck>", "attr": "<attribute name>", "value": "<new value as a string>"}}
  ]
}}

Rules:
- Every xpath and attr you use MUST correspond to an element/attribute you can literally see in the anchor deck content above. Do not guess.
- Only propose edits to attribute VALUES that already exist. Never invent new elements or attributes.
- Use standard ElementTree xpath syntax, e.g. ".//FieldSpecification[@name='sourceTerm']".
- If the anchor deck matches the question with no changes needed, return an empty edits list.
"""


def build_prompt(question, geos_root):
    blocks = []
    for d in ANCHOR_DECKS:
        full_path = os.path.join(geos_root, d["relpath"])
        with open(full_path) as f:
            content = f.read()
        blocks.append(
            f"=== {d['filename']} ===\n"
            f"Description: {d['description']}\n"
            f"Content:\n{content}\n"
        )
    anchor_contents = "\n".join(blocks)
    return PROMPT_TEMPLATE.format(anchor_contents=anchor_contents, question=question)


def extract_json(text):
    cleaned = text.strip()
    cleaned = re.sub(r'<think>.*?</think>', '', cleaned, flags=re.DOTALL).strip()
    cleaned = re.sub(r'^```(json)?', '', cleaned).strip()
    cleaned = re.sub(r'```$', '', cleaned).strip()

    start = cleaned.find('{')
    end = cleaned.rfind('}')
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object found in LLM output:\n{text}")
    return json.loads(cleaned[start:end + 1])


def apply_edits(anchor_path, edits, output_path):
    tree = ET.parse(anchor_path)
    root = tree.getroot()
    applied = []

    for edit in edits:
        if edit["op"] != "set_attribute":
            raise ValueError(f"Unsupported edit op: {edit['op']}")

        element = root.find(edit["xpath"])
        if element is None:
            raise ValueError(
                f"xpath '{edit['xpath']}' did not resolve to any element "
                f"in the anchor deck. Refusing to apply this edit."
            )
        if edit["attr"] not in element.attrib:
            raise ValueError(
                f"Attribute '{edit['attr']}' does not exist on element "
                f"matched by '{edit['xpath']}' (existing attrs: "
                f"{list(element.attrib.keys())}). Refusing to add a new attribute."
            )

        old_value = element.attrib[edit["attr"]]
        element.set(edit["attr"], str(edit["value"]))
        applied.append({
            "xpath": edit["xpath"], "attr": edit["attr"],
            "old_value": old_value, "new_value": str(edit["value"]),
        })

    tree.write(output_path, encoding="unicode", xml_declaration=True)
    return applied


def synthesize_deck(question, geos_root, output_path, use_api=False, provider="openai", model=None, **llm_kwargs):
    prompt = build_prompt(question, geos_root)
    raw_response = call_llm(prompt, use_api=use_api, provider=provider, model=model, **llm_kwargs)
    parsed = extract_json(raw_response)

    anchor_meta = get_anchor_by_filename(parsed["anchor"])
    anchor_path = os.path.join(geos_root, anchor_meta["relpath"])

    applied = apply_edits(anchor_path, parsed.get("edits", []), output_path)
    lint_result = lint_deck(output_path)

    return {
        "question": question,
        "anchor_chosen": parsed["anchor"],
        "llm_reasoning": parsed.get("reasoning"),
        "edits_applied": applied,
        "lint_report": lint_result.report(),
        "lint_clean": not lint_result.has_errors,
        "output_path": output_path,
        "raw_llm_response": raw_response,
    }
