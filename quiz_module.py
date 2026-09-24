import json
import re

from pydantic import BaseModel, Field

from gemini_client import generate_text


# --------------------------------------------------
# Quiz question structure
# --------------------------------------------------

class QuizQuestion(BaseModel):

    question: str

    options: list[str] = Field(
        min_length=4,
        max_length=4
    )

    correct_answer: str

    explanation: str


# --------------------------------------------------
# Quiz response structure
# --------------------------------------------------

class QuizResponse(BaseModel):

    questions: list[QuizQuestion] = Field(
        min_length=3,
        max_length=3
    )


# --------------------------------------------------
# Clean Gemini JSON
# --------------------------------------------------

def clean_json_block(text):

    text = text.strip()

    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


# --------------------------------------------------
# Generate quiz
# --------------------------------------------------

def generate_quiz(passage):

    prompt = f"""
Create exactly 3 multiple-choice questions
from the following educational content.

CONTENT:
{passage}

Requirements:

- Exactly 3 questions.
- Exactly 4 options for every question.
- Only one correct answer.
- Options must be relevant.
- Questions must be based only on the content.
- Include a short explanation.
"""

    schema = QuizResponse.model_json_schema()

    response = generate_text(
        prompt=prompt,
        system_instruction=(
            "You are an educational MCQ generator."
        ),
        temperature=0.3,
        max_output_tokens=1600,
        response_mime_type="application/json",
        response_schema=schema
    )

    cleaned = clean_json_block(
        response
    )

    try:

        quiz = QuizResponse.model_validate_json(
            cleaned
        )

    except Exception:

        try:

            data = json.loads(
                cleaned
            )

            quiz = QuizResponse.model_validate(
                data
            )

        except Exception as e:

            raise RuntimeError(
                f"Quiz JSON parsing failed: {e}"
            )

    return [
        question.model_dump()
        for question in quiz.questions
    ]