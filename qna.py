from gemini_client import generate_text


def answer_question(question):

    prompt = f"""
You are EduGenie, an AI educational assistant.

Answer the student's question clearly and accurately.

Student Question:
{question}

Instructions:

1. Give the direct answer first.
2. Explain the answer in simple language.
3. Use an example when useful.
4. Avoid unnecessary technical words.
5. Do not invent information.
6. If the question is unclear, mention what is unclear.
7. Keep the answer useful for a student.
"""

    return generate_text(
        prompt=prompt,
        system_instruction=(
            "You are a helpful and accurate "
            "educational tutor."
        ),
        temperature=0.3,
        max_output_tokens=900
    )