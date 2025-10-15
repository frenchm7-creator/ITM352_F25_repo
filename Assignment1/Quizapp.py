# Assignment 1.  Build a quiz app to:
# Ask multiple-choice questions and read from a JSON file.
# Check answers and keep track of the user's score.
# Write the score history out to a file.
# Notify the user when they get a new high score.
# Name: Micah French
# Date: October 14, 2025

from string import ascii_lowercase
import random
import json
import os
from datetime import datetime  

# Files for questions and score history
QUESTION_FILE = 'questions.json'
SCORES_FILE = 'scores.json'

# Read questions from JSON file
question_file = open(QUESTION_FILE)
QUESTIONS = json.load(question_file)
question_file.close()

# Prepare a list of questions for the quiz.
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    # Randomly select a subset of questions for the quiz
    return random.sample(list(questions.items()), num_questions)

# Get an answer from the user, ensuring it is one of the valid choices.
def get_answer(question, alternatives):
    print(f"\n{question}?")
    labelled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, len(alternatives))))
    for label, alternative in labelled_alternatives.items():
        print(f" {label}. {alternative}")

    # Loop until the user provides a valid answer
    while (answer_label := input("\nChoice? ").lower()) not in labelled_alternatives:
        print(f"Please answer one of {', '.join(labelled_alternatives)}")
    return labelled_alternatives.get(answer_label)

# Ask one question and return 1 if correct, 0 otherwise
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, len(alternatives))
    answer = get_answer(question, ordered_alternatives)

    if answer == correct_answer:
        print("* Correct! *")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}")
        return 0

# Get the highest score recorded
def get_high_score():
    if not os.path.exists(SCORES_FILE):
        return 0
    try:
        with open(SCORES_FILE, 'r') as file:
            scores = json.load(file)
            if not scores:
                return 0
            return max(entry['score'] for entry in scores)
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

    with open(SCORES_FILE, 'w') as file:
        json.dump(scores, file, indent=4)

# Main program
print("Welcome to the Quiz!\n")
user_name = input("Enter your name: ")

NUM_QUESTIONS_PER_QUIZ = 5
num_correct = 0

# get previous high score
previous_high = get_high_score()

# prepare and ask questions
questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)
for num, (question, alternatives) in enumerate(questions, 1):
    print(f"\nQuestion {num}:")
    num_correct += ask_question(question, alternatives)

# display final results
print(f"\nYou got {num_correct} out of {len(questions)} questions correct.")

# record the score
record_score(user_name, num_correct, len(questions))

# check for new high score
if num_correct > previous_high:
    print(f"\nCongratulations {user_name}! New high score: {num_correct}")
else:
    print(f"Your highest score to beat is {previous_high}.")
