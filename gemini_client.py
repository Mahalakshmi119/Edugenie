import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# --------------------------------------------------
# Load .env
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Configuration
# --------------------------------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash-lite"
)


# --------------------------------------------------
# Gemini client
# --------------------------------------------------

client = None

if GEMINI_API_KEY:

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )


# --------------------------------------------------
# Check client
# --------------------------------------------------

def get_client():

    if client is None:

        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key "
            "inside the .env file."
        )

    return client


# --------------------------------------------------
# Generate text
# --------------------------------------------------

def generate_text(
    prompt,
    system_instruction=None,
    temperature=0.4,
    max_output_tokens=1000,
    response_mime_type=None,
    response_schema=None
):

    gemini = get_client()

    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )

    if system_instruction:

        config.system_instruction = (
            system_instruction
        )

    if response_mime_type:

        config.response_mime_type = (
            response_mime_type
        )

    if response_schema:

        config.response_schema = (
            response_schema
        )

    response = gemini.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config
    )

    if not response.text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return response.text.strip()