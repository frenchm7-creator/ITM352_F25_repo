# Use of AI: Assignment 3

This document explains how AI (ChatGPT) was used to support development, and highlights learning outcomes, template structure, routes, and testing with `pytest`.

---

## 1. Template Inheritance

- Created `base.html` to define common **header** and **footer** for all pages.
- Child templates (`index.html`, `quiz.html`, `result.html`) **extend** `base.html` using:

```html
{% extends "base.html" %}
{% block content %}
  <!-- page-specific content -->
{% endblock %}
```

- Learned to reuse header, navigation, and footer consistently across pages.
- Flash messages and dynamic content are handled in `base.html` to avoid duplication.

---

## 2. Flask Routes

Implemented routes as per assignment requirements:

- `/` – Home page, name input, and previous score history.
- `/start` – Initializes a new quiz, stores questions in session, redirects to `/quiz`.
- `/quiz` – Displays current question and choices.
- `/answer` – Handles answer submission, updates score, moves to next question.
- `/result` – Shows final score, user rank, and leaderboard.
- `/leaderboard` – Displays top 10 scores.
- `/api/questions` – Returns all questions in JSON format.
- `/api/scores` – Returns all recorded scores in JSON format.

**Learning:**

- Learned to design RESTful endpoints for data retrieval.
- Used `session`, `flash`, and redirects to manage user state and feedback.

---

## 3. Data Handling

- Questions stored in `questions.json` and scores in `scores.json`.
- Randomized question order and answer choices for each quiz session.
- Score is recorded with timestamp for leaderboard and history.

**Learning:**

- Learned JSON read/write with Python.
- Managed persistent state using Flask sessions.

---

## 4. Testing with Pytest

- **Unit tests**: Verified helper functions like `load_questions()` and `record_score()`.
- **Integration tests**: Used `Flask.test_client` to simulate the user actions.

Example:

```python
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your name" in response.data
```

**Learning:**

- Learned to structure tests for unit, integration, and simulated user flows.
- Verified that core functionalities and routes work as intended.

---

## 5. Learning Outcomes from AI Support

- Learned to use AI for small components like:
  - Flask routes and endpoint logic.
  - Pytest test scaffolding.
  - Template inheritance examples.
- Adapted AI-generated code to **fully understand** its working.
- Ensured AI code meets assignment requirements and follows Python/Flask conventions.

---

## 6. Summary

- Used template inheritance for reusable UI elements.
- Implemented all required routes, sessions, and flash messages.
- Managed data in JSON files and randomized quiz sessions.
- Wrote tests with `pytest` for unit, integration, and simulated user flows.
- Reflected on learning and AI usage throughout the project.