import os

from dotenv import load_dotenv
from gemini_client import generate_text


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()


MODEL_NAME = os.getenv(
    "LOCAL_EXPLANATION_MODEL",
    "MBZUAI/LaMini-Flan-T5-783M"
)

EXPLANATION_MODE = os.getenv(
    "EXPLANATION_MODE",
    "gemini"
).lower()


# --------------------------------------------------
# Local model
# --------------------------------------------------

_local_model = None
_local_tokenizer = None
_local_device = None


def load_local_model():

    global _local_model
    global _local_tokenizer
    global _local_device

    if _local_model is not None:

        return (
            _local_tokenizer,
            _local_model,
            _local_device
        )

    import torch

    from transformers import (
        AutoTokenizer,
        AutoModelForSeq2SeqLM
    )

    print(
        "Loading local explanation model..."
    )

    _local_tokenizer = (
        AutoTokenizer.from_pretrained(
            MODEL_NAME
        )
    )

    _local_model = (
        AutoModelForSeq2SeqLM.from_pretrained(
            MODEL_NAME
        )
    )

    if torch.cuda.is_available():

        _local_device = "cuda"

    else:

        _local_device = "cpu"

    _local_model.to(
        _local_device
    )

    _local_model.eval()

    return (
        _local_tokenizer,
        _local_model,
        _local_device
    )


# --------------------------------------------------
# Local explanation
# --------------------------------------------------

def explain_with_local_model(topic):

    tokenizer, model, device = (
        load_local_model()
    )

    prompt = f"""
Explain this topic to a beginner:

{topic}

Use simple language.

Include:

1. Definition
2. Important points
3. Simple example
4. Short recap
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    outputs = model.generate(
        **inputs,
        max_new_tokens=220,
        num_beams=4
    )

    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    if not result.strip():

        raise RuntimeError(
            "Local model returned empty output."
        )

    return result.strip()


# --------------------------------------------------
# Gemini explanation
# --------------------------------------------------

def explain_with_gemini(topic):

    prompt = f"""
Explain the following topic to a beginner:

{topic}

Use:

Definition:
Key Points:
Example:
Recap:

Use very simple language.
"""

    return generate_text(
        prompt=prompt,
        system_instruction=(
            "You are a beginner-friendly "
            "educational tutor."
        ),
        temperature=0.3,
        max_output_tokens=700
    )


# --------------------------------------------------
# Main explanation function
# --------------------------------------------------

def explain_topic(topic):

    if EXPLANATION_MODE == "local":

        return explain_with_local_model(
            topic
        )

    if EXPLANATION_MODE == "gemini":

        return explain_with_gemini(
            topic
        )

    # Auto mode

    try:

        return explain_with_local_model(
            topic
        )

    except Exception as local_error:

        print(
            "Local model failed:",
            local_error
        )

        return explain_with_gemini(
            topic
        )