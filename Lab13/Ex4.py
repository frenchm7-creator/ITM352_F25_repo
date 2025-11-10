from flask import Flask, request, redirect, url_for, render_template_string, session
import json, os, random
from datetime import datetime
from string import ascii_lowercase

app = Flask(__name__)
app.secret_key = os.urandom(24)

QUESTION_FILE = "questions.json"
SCORES_FILE = "scores.json"
NUM_QUESTIONS_PER_QUIZ = 5

# load questions (keep file next to this script)
base_dir = os.path.dirname(os.path.abspath(__file__))
questions_path = os.path.join(base_dir, QUESTION_FILE)
with open(questions_path, "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# helpers for score persistence
def get_high_score():
    path = os.path.join(base_dir, SCORES_FILE)
    if not os.path.exists(path):
        return 0
    try:
        with open(path, "r", encoding="utf-8") as fh:
            scores = json.load(fh) or []
        return max((e.get("score", 0) for e in scores), default=0)
    except Exception:
        return 0

def record_score(name, score, total):
    path = os.path.join(base_dir, SCORES_FILE)
    entry = {"name": name, "score": score, "total": total, "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
    scores = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                scores = json.load(fh) or []
        except json.JSONDecodeError:
            scores = []
    scores.append(entry)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(scores, fh, indent=2)

# pages / routes
INDEX_HTML = """<!doctype html>
<title>Quiz</title>
<h1>Welcome to the Quiz</h1>
<form method="post" action="{{ url_for('start') }}">
  Your name: <input name="name" required>
  <button type="submit">Start Quiz</button>
</form>
"""

QUIZ_HTML = """<!doctype html>
<title>Quiz Questions</title>
<h1>Quiz for {{ name }}</h1>
<form method="post" action="{{ url_for('grade') }}">
  {% for i,q in enumerate(questions) %}
    <fieldset>
      <legend>Q{{ i+1 }}. {{ q.q }}</legend>
      {% for opt in q.options %}
        <label>
          <input type="radio" name="ans_{{ i }}" value="{{ opt }}" required> {{ opt }}
        </label><br>
      {% endfor %}
    </fieldset>
    <br>
  {% endfor %}
  <button type="submit">Submit Answers</button>
</form>
"""

RESULT_HTML = """<!doctype html>
<title>Results</title>
<h1>Results for {{ name }}</h1>
<p>You scored {{ score }} out of {{ total }}.</p>
{% if new_high %}
  <p><strong>New high score! 🎉</strong></p>
{% else %}
  <p>Current high score to beat: {{ high_score }}</p>
{% endif %}
<p><a href="{{ url_for('index') }}">Play again</a></p>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)

@app.route("/start", methods=["POST"])
def start():
    name = request.form.get("name", "").strip() or "Player"
    # prepare questions: random sample of items
    items = random.sample(list(QUESTIONS.items()), min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS)))
    prepared = []
    for q_text, alternatives in items:
        # alternatives list: correct answer expected at index 0 in source file
        correct = alternatives[0]
        opts = random.sample(alternatives, len(alternatives))
        prepared.append({"q": q_text, "options": opts, "correct": correct})
    # store in session
    session["name"] = name
    session["questions"] = prepared
    return redirect(url_for("quiz"))

@app.route("/quiz", methods=["GET"])
def quiz():
    name = session.get("name")
    questions = session.get("questions")
    if not questions:
        return redirect(url_for("index"))
    return render_template_string(QUIZ_HTML, name=name, questions=questions)

@app.route("/grade", methods=["POST"])
def grade():
    questions = session.get("questions", [])
    name = session.get("name", "Player")
    score = 0
    for i, q in enumerate(questions):
        key = f"ans_{i}"
        ans = request.form.get(key)
        if ans is None:
            continue
        if ans == q.get("correct"):
            score += 1
    total = len(questions)
    previous_high = get_high_score()
    record_score(name, score, total)
    new_high = score > previous_high
    # clear session quiz
    session.pop("questions", None)
    return render_template_string(RESULT_HTML, name=name, score=score, total=total, new_high=new_high, high_score=previous_high)

if __name__ == "__main__":
    app.run(debug=True)