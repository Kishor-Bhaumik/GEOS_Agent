"""
LLM backend wrapper for the GEOS agent.

call_llm(prompt, use_api=False, provider="openai", model=None) -> str
  use_api=False           -> local HuggingFace Qwen model
  use_api=True, provider="openai"   -> OpenAI API (default, cheap steps)
  use_api=True, provider="deepseek" -> DeepSeek API (expensive reasoning steps only)
"""
import os

_LOCAL_MODEL = None
_LOCAL_TOKENIZER = None

LOCAL_MODEL_NAME = os.environ.get("GEOSAGENT_LOCAL_MODEL", "Qwen/Qwen3.8-27B")
DEFAULT_OPENAI_MODEL = os.environ.get("GEOSAGENT_API_MODEL", "gpt-4o-mini")
DEFAULT_DEEPSEEK_MODEL = os.environ.get("GEOSAGENT_DEEPSEEK_MODEL", "deepseek-v4-pro")


def _load_local_model():
    global _LOCAL_MODEL, _LOCAL_TOKENIZER
    if _LOCAL_MODEL is not None:
        return _LOCAL_MODEL, _LOCAL_TOKENIZER
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    print(f"[llm_backend] Loading local model: {LOCAL_MODEL_NAME} ...")
    _LOCAL_TOKENIZER = AutoTokenizer.from_pretrained(LOCAL_MODEL_NAME)
    _LOCAL_MODEL = AutoModelForCausalLM.from_pretrained(
        LOCAL_MODEL_NAME, torch_dtype=torch.bfloat16, device_map="auto",
    )
    print("[llm_backend] Local model loaded.")
    return _LOCAL_MODEL, _LOCAL_TOKENIZER


def _call_local(prompt, max_new_tokens=3000, temperature=0.0, **_ignored):
    model, tokenizer = _load_local_model()
    messages = [{"role": "user", "content": prompt}]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt",
        return_dict=True, enable_thinking=False,
    ).to(model.device)
    output_ids = model.generate(
        **inputs, max_new_tokens=max_new_tokens,
        do_sample=(temperature > 0), temperature=max(temperature, 1e-5),
    )
    generated = output_ids[0][inputs["input_ids"].shape[-1]:]
    return tokenizer.decode(generated, skip_special_tokens=True)


def _call_openai(prompt, model=None, max_tokens=1500, **_ignored):
    from openai import OpenAI
    client = OpenAI()  # reads OPENAI_API_KEY from env
    response = client.chat.completions.create(
        model=model or DEFAULT_OPENAI_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def _call_deepseek(prompt, model=None, max_tokens=1500, **_ignored):
    from openai import OpenAI
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    )
    response = client.chat.completions.create(
        model=model or DEFAULT_DEEPSEEK_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content




def _call_qwen(prompt, model=None, max_tokens=6000, enable_thinking=True, **_ignored):
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )
    response = client.chat.completions.create(
        model=model or "qwen/qwen3.8-27b",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
        extra_body={"reasoning": {"enabled": enable_thinking}},
    )
    return response.choices[0].message.content


def call_llm(prompt, use_api=False, provider="openai", model=None, **kwargs):
    """
    provider only matters when use_api=True. "openai" (default) for cheap
    routine steps (plan, synthesize, probe). "deepseek" for the expensive
    reasoning step only - pass explicitly where needed.
    """
    if not use_api:
        return _call_local(prompt, **kwargs)
    if provider == "deepseek":
        return _call_deepseek(prompt, model=model, **kwargs)
    if provider == "qwen":
        return _call_qwen(prompt, model=model, **kwargs)
    return _call_openai(prompt, model=model, **kwargs)
