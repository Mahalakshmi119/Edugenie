# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is an AI-powered learning assistant designed to help students learn, understand, practice, and revise educational topics using Google Gemini.

## Features

* Question & Answer
* Simplified Topic Explanation
* Quiz Generation
* Text Summarization
* Personalized Learning Recommendations

## Technologies Used

* Python
* FastAPI
* Google Gemini API
* HTML
* CSS
* Jinja2
* Uvicorn
* Pydantic

## Project Structure

```text
EduGenie/
│
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── tests/
    └── test_api.py
```

## Requirements

Before running the project, install:

* Python 3.10 or above
* FastAPI
* Uvicorn
* Google Gemini API key
* Jinja2
* Python dotenv

## Installation

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
GEMINI_MODEL=YOUR_GEMINI_MODEL
EXPLANATION_MODE=gemini
LOCAL_EXPLANATION_MODEL=MBZUAI/LaMini-Flan-T5-783M
```

Replace:

```text
YOUR_GEMINI_API_KEY_HERE
```

with your actual Gemini API key.

## Run the Application

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

After the server starts, open:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Question & Answer

```text
POST /qa
```

Used to answer student questions.

### Explanation

```text
POST /explain
```

Used to explain a topic in simple language.

### Quiz

```text
POST /quiz
```

Generates multiple-choice questions from educational content.

### Summarization

```text
POST /summarize
```

Summarizes educational text for quick revision.

### Learning Recommendations

```text
POST /learn/recommendations
```

Creates a personalized learning path for a topic.

## How EduGenie Works

```text
Student
   ↓
EduGenie Web Interface
   ↓
FastAPI Backend
   ↓
Selected Learning Module
   ↓
Google Gemini API
   ↓
AI Generated Response
   ↓
Student
```

## Testing

Run the automated tests using:

```bash
pytest
```

The project includes tests for:

* Home page
* Health check
* Question & Answer
* Explanation
* Quiz
* Summary
* Learning recommendations

## Example Questions

### Q&A

```text
What is machine learning?
```

### Explanation

```text
Explain artificial intelligence to a beginner.
```

### Quiz

```text
Machine Learning
```

### Summary

```text
Paste your educational notes here.
```

### Learning Path

```text
Python programming for beginners
```

## Future Enhancements

Possible future improvements include:

* User login and authentication
* Student progress tracking
* Difficulty-based quizzes
* Learning history
* Voice-based learning
* More AI models
* Database integration
* Mobile application
Project Goal

The goal of EduGenie is to provide students with an easy-to-use AI learning assistant that can answer questions, simplify difficult topics, generate quizzes, summarize study materials, and recommend personalized learning paths.