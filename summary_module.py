from gemini_client import generate_text


def summarize_text(text):

    prompt = f"""
You are EduGenie.

Summarize the following educational content.

CONTENT:
{text}

Return the response in this format:

Summary:
A short easy-to-understand summary.

Important Points:
- Point 1
- Point 2
- Point 3

Key Terms:
- Term 1
- Term 2
- Term 3

Important rules:

- Preserve the original meaning.
- Do not add unsupported information.
- Make it useful for quick revision.
- Use simple student-friendly language.
"""

    return generate_text(
        prompt=prompt,
        system_instruction=(
            "You are an expert educational "
            "summarization assistant."
        ),
        temperature=0.2,
        max_output_tokens=1000
    )