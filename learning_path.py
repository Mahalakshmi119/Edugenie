from gemini_client import generate_text


def get_learning_recommendations(topic):

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a structured learning path for:

TOPIC:
{topic}

Create the following sections:

1. Learning Goal

2. Beginner Level
   - Topics to learn
   - Basic practice

3. Intermediate Level
   - Topics to learn
   - Practice activities

4. Advanced Level
   - Advanced topics
   - Projects

5. Suggested Timeline

6. Practice Plan

7. Recommended Resource Types
   - Videos
   - Articles
   - Books
   - Documentation

8. Final Revision Plan

Assume the learner is a beginner unless
the input clearly specifies another level.

Make the learning path practical and sequential.
"""

    return generate_text(
        prompt=prompt,
        system_instruction=(
            "You are an expert learning-path "
            "designer for students."
        ),
        temperature=0.4,
        max_output_tokens=1400
    )