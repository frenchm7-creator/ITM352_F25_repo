"""
Flask web application version of the Assignment 1 quiz app.

This application:
- Reuses logic and structure from the console-based quiz (Assignment 1).
- Adds a web UI with Flask templates and static CSS.
- Tracks user sessions to identify returning users.
- Stores and retrieves user scores in a JSON file (persistent score history).
- Randomizes question selection and answer options each quiz session.
- Provides immediate feedback on answers via flash messages.
- Computes and displays a leaderboard with top scores.
- Includes simple RESTful API endpoints for questions and scores.
- Handles errors and invalid inputs gracefully.

AI usage:
- Portions of Flask routing and template scaffolding were generated with ChatGPT.
  See use_of_ai.md for details and prompts used.

Name: Micah French
Date: 
"11/14/25"


from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from string import ascii_lowercase
import random
import json
import os
from datetime import datetime

# Configuration 
# Secret key is required for session management and flash messages.
APP_SECRET = "replace_with_a_random_secret_for_production"  
QUESTION_FILE = os.path.join("data", "questions.json")
SCORES_FILE = os.path.join("data", "scores.json")
NUM_QUESTIONS_PER_QUIZ = 5

app = Flask(__name__)
app.secret_key = APP_SECRET

# Reused/Adapted Assignment 1 code 

# Read questions from JSON file 
def load_questions():
    if not os.path.exists(QUESTION_FILE):
        return {}
    with open(QUESTION_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Prepare a list of questions for the quiz.
def prepare_questions(questions, num_questions):
    """
    Reused function from Assignment 1, adapted to return a list of dicts
    where each dict contains: 'question', 'choices' (shuffled list), 'correct'
    """
    num_questions = min(num_questions, len(questions))
    sampled = random.sample(list(questions.items()), num_questions)
    prepared = []
    for question_text, alternatives in sampled:
        correct_answer = alternatives[0]
        shuffled = random.sample(alternatives, len(alternatives))
        prepared.append({
            "question": question_text,
            "choices": shuffled,
            "correct": correct_answer,
        })
    return prepared

# Get the highest score recorded
def get_high_score():
    if not os.path.exists(SCORES_FILE):
        return 0
    try:
        with open(SCORES_FILE, 'r') as file:
            scores = json.load(file)
            if not scores:
                return 0
            return max(entry.get('score', 0) for entry in scores)
    except (json.JSONDecodeError, KeyError):
        return 0

# Save the user's score into the JSON file
def record_score(name, score, total):
    entry = {
        "name": name,
        "score": score,
        "total": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r') as file:
                scores = json.load(file)
        except json.JSONDecodeError:
            scores = []
    else:
        scores = []

    scores.append(entry)

    # Persist
    with open(SCORES_FILE, 'w') as file:
        json.dump(scores, file, indent=4)

# Load all scores (helper)
def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Compute top N leaderboard entries
def get_leaderboard(top_n=10):
    scores = load_scores()
    # Sort by score desc, then recent date desc
    sorted_scores = sorted(scores, key=lambda e: (e.get('score', 0), e.get('date', '')), reverse=True)
    return sorted_scores[:top_n]


# Flask routes 

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Home page / login:
    - If user submits name, save to session and redirect to /start
    - If user returns and session['username'] exists, show welcome and history
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            flash("Please enter a valid name.", "error")
            return redirect(url_for("index"))
        session['username'] = name
        # On starting new session, clear any previous quiz state
        session.pop('quiz_questions', None)
        session.pop('current_index', None)
        session.pop('score', None)
        return redirect(url_for("start_quiz"))
    # GET: show homepage with optional history if username in session
    username = session.get('username')
    user_scores = []
    if username:
        all_scores = load_scores()
        user_scores = [s for s in all_scores if s.get('name') == username]
        # sort descending by date (most recent first)
        user_scores = sorted(user_scores, key=lambda x: x.get('date', ''), reverse=True)
    return render_template("index.html", username=username, user_scores=user_scores)

@app.route("/start")
def start_quiz():
    """
    Initialize a quiz:
    - Load questions from file
    - Prepare randomized questions
    - Store prepared questions in session (JSON-serializable)
    - Initialize current_index and score, then redirect to /quiz
    """
    questions_map = load_questions()
    if not questions_map:
        return render_template("error.html", message="No questions available. Please check questions.json.")
    prepared = prepare_questions(questions_map, NUM_QUESTIONS_PER_QUIZ)
    # store in session
    session['quiz_questions'] = prepared
    session['current_index'] = 0
    session['score'] = 0
    # For persistent identification, ensure username exists
    if 'username' not in session:
        # ask user to provide name on index page
        flash("Please enter your name before starting the quiz.", "info")
        return redirect(url_for('index'))
    return redirect(url_for("quiz"))

@app.route("/quiz", methods=["GET"])
def quiz():
    """
    Show the current question based on session['current_index'].
    """
    quiz_questions = session.get('quiz_questions')
    idx = session.get('current_index', 0)
    score = session.get('score', 0)

    if not quiz_questions:
        flash("No active quiz. Start a new quiz.", "error")
        return redirect(url_for("index"))

    if idx >= len(quiz_questions):
        return redirect(url_for("result"))

    current = quiz_questions[idx]
    # label choices a,b,c,d...
    labels = list(ascii_lowercase)[:len(current['choices'])]
    labeled_choices = list(zip(labels, current['choices']))
    return render_template("quiz.html",
                           question=current['question'],
                           choices=labeled_choices,
                           index=idx + 1,
                           total=len(quiz_questions),
                           score=score)

@app.route("/answer", methods=["POST"])
def answer():
    """
    Handle answer submission:
    - Validate input
    - Update score and current index in session
    - Provide immediate feedback (flash messages)
    - Then redirect to /quiz (next question) or /result if finished
    """
    selected_label = request.form.get("choice")
    if selected_label is None:
        flash("Please select an answer before submitting.", "error")
        return redirect(url_for("quiz"))

    # Load session quiz and state
    quiz_questions = session.get('quiz_questions')
    idx = session.get('current_index', 0)

    if not quiz_questions or idx >= len(quiz_questions):
        flash("Invalid quiz state. Start a new quiz.", "error")
        return redirect(url_for("index"))

    current = quiz_questions[idx]
    labels = list(ascii_lowercase)[:len(current['choices'])]
    try:
        label_index = labels.index(selected_label)
    except ValueError:
        flash("Invalid choice submitted.", "error")
        return redirect(url_for("quiz"))

    selected_answer = current['choices'][label_index]
    correct_answer = current['correct']

    # Update score
    if selected_answer == correct_answer:
        session['score'] = session.get('score', 0) + 1
        flash("Correct!", "success")
    else:
        flash(f"Incorrect. Correct answer: {correct_answer}", "info")

    # move to next
    session['current_index'] = idx + 1

    # if finished, redirect to result
    if session['current_index'] >= len(quiz_questions):
        return redirect(url_for("result"))
    else:
        return redirect(url_for("quiz"))

@app.route("/result", methods=["GET"])
def result():
    """
    Show final results, record the score in persistent store (scores.json),
    and display a small summary and link to leaderboard.
    """
    username = session.get('username')
    if username is None:
        flash("No username in session. Please enter your name.", "error")
        return redirect(url_for("index"))

    score = session.get('score', 0)
    quiz_questions = session.get('quiz_questions', [])
    total = len(quiz_questions)

    # record the score (persist)
    record_score(username, score, total)

    # Prepare summary for display: number correct/incorrect
    incorrect = total - score
    # compute leaderboard and user rank
    leaderboard = get_leaderboard(10)
    # Determine user's best rank (most recent rank computing)
    all_scores = load_scores()
    # compute sorted list positions
    sorted_scores = sorted(all_scores, key=lambda e: (e.get('score', 0), e.get('date', '')), reverse=True)
    user_rank = None
    for i, entry in enumerate(sorted_scores, start=1):
        if entry.get('name') == username and entry.get('score') == score and entry.get('date'):
            user_rank = i
            break

    # Clear quiz state so the user can start a fresh quiz next time
    session.pop('quiz_questions', None)
    session.pop('current_index', None)
    session.pop('score', None)

    return render_template("result.html",
                           username=username,
                           score=score,
                           total=total,
                           incorrect=incorrect,
                           leaderboard=leaderboard,
                           user_rank=user_rank)

@app.route("/leaderboard")
def leaderboard_page():
    leaderboard = get_leaderboard(10)
    return render_template("leaderboard.html", leaderboard=leaderboard)

# Simple API routes (RESTful style) 
@app.route("/api/questions", methods=["GET"])
def api_questions():
    #returns all questions available (not the prepared quiz).
    questions_map = load_questions()
    return jsonify(questions_map)

@app.route("/api/scores", methods=["GET"])
def api_scores():
    # returns all recorded scores
    return jsonify(load_scores())

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", message="Page not found (404)."), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", message="An internal server error occurred."), 500

if __name__ == "__main__":
    app.run(debug=True)
