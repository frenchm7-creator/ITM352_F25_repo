import pytest
import os
import json
from app import app, prepare_questions, record_score, load_scores, get_leaderboard

@pytest.fixture
def client():
    """Flask test client with TESTING enabled."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

@pytest.fixture
def temp_scores_file(tmp_path, monkeypatch):
    """Use a temporary file for scores to avoid modifying real data."""
    tmp_file = tmp_path / "scores.json"
    monkeypatch.setattr("app.SCORES_FILE", tmp_file)
    return tmp_file

@pytest.fixture
def sample_questions():
    """Sample questions dictionary for unit tests."""
    return {
        "Q1": ["A", "B", "C", "D"],
        "Q2": ["True", "False"]
    }

# UNIT TESTS
def test_prepare_questions_returns_correct_format(sample_questions):
    prepared = prepare_questions(sample_questions, 2)
    assert len(prepared) == 2
    for q in prepared:
        assert 'question' in q
        assert 'choices' in q
        assert 'correct' in q
        # Correct answer should be in choices
        assert q['correct'] in q['choices']
        # Choices are shuffled
        assert set(q['choices']) == set(sample_questions[q['question']])

def test_record_and_load_scores(temp_scores_file):
    # Initially empty
    scores = load_scores()
    assert isinstance(scores, list)
    # Record a new score
    record_score("Alice", 3, 5)
    scores = load_scores()
    assert len(scores) == 1
    assert scores[0]['name'] == "Alice"
    assert scores[0]['score'] == 3
    assert scores[0]['total'] == 5

def test_get_leaderboard_returns_top_scores(temp_scores_file):
    record_score("Alice", 3, 5)
    record_score("Bob", 5, 5)
    record_score("Charlie", 4, 5)
    top = get_leaderboard(top_n=2)
    assert len(top) == 2
    assert top[0]['score'] >= top[1]['score']

# INTEGRATION TESTS (FLASK ROUTES)
def test_home_page(client):
    """Home page loads and shows input form."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Enter your name" in resp.data

def test_start_quiz_redirect(client, monkeypatch, sample_questions):
    """POST name and redirect to /start"""
    monkeypatch.setattr("app.load_questions", lambda: sample_questions)
    resp = client.post("/", data={"name": "TestUser"}, follow_redirects=True)
    assert resp.status_code == 200
    # After redirect, should show quiz page
    assert b"Question" in resp.data or b"No active quiz" in resp.data

def test_leaderboard_page(client, temp_scores_file):
    """Leaderboard page loads"""
    # Add sample scores
    record_score("Alice", 3, 5)
    record_score("Bob", 5, 5)
    resp = client.get("/leaderboard")
    assert resp.status_code == 200
    assert b"Leaderboard" in resp.data

def test_api_questions(client, monkeypatch, sample_questions):
    """API endpoint for questions returns JSON"""
    monkeypatch.setattr("app.load_questions", lambda: sample_questions)
    resp = client.get("/api/questions")
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "Q1" in data

def test_api_scores(client, temp_scores_file):
    """API endpoint for scores returns JSON"""
    record_score("Alice", 3, 5)
    resp = client.get("/api/scores")
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    data = resp.get_json()
    assert isinstance(data, list)
    assert any(s['name'] == "Alice" for s in data)
