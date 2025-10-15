# Quiz 7.  Put questions and answers into a dictionary, to
# include answer options.
# Allow the user to select the correct answer by its label.
# Improve look and usability. Keep track of correct answers.
# Loop until the user provides a valid answer.
# Randomize the order of questions and answers.
# Refactor the code to use functions.
# Name: Micah French
# Date: October 8, 2025

from string import ascii_lowercase
import random

# Quiz questions. For each question list the possible answers, with the first answer being the correct one.
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "13", "24", "36", "48"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "Waco"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "Which class novel opens with the line 'Call Me Ishmael'": ["Moby Dick", "The Great Gatsby", "1984", "To Kill a Mockingbird"]
}

# Prepare a list of questions for the quiz.
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    # Randomly select a subset of questions for the quiz
    return random.sample(list(questions.items()), num_questions)

# Get an answer from the user, ensuring it is one of the valid choices.
def get_answer(question, alternatives):
    print(f"\n{question}? ")
    labelled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives,len(alternatives))))
    for label, alternative in labelled_alternatives.items():
        print(f" {label}. {alternative}")

    # Loop until the user provides a valid answer
    while (answer_label := input("\nChoice? ")) not in labelled_alternatives:
        print(f"Please answer one of {', '.join(labelled_alternatives)}")
    return labelled_alternatives.get(answer_label)

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, len(alternatives))
    answer = get_answer(question, ordered_alternatives)

    if answer == correct_answer:
        print("* Correct! *")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

num_correct = 0
NUM_QUESTIONS_PER_QUIZ = 5

# Main quiz loop.
questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)
for num, (question, alternatives) in enumerate(questions, 1):
    print(f"\nQuestion {num}:")
    num_correct += ask_question(question, alternatives)
    

print(f"\nYou got {num_correct} out of {len(questions)} questions correct.")