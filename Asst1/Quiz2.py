# Quiz 2.  Put questions and answers into a list
# Name: Micah French
# Date: October 3, 2025

QUESTIONS = [
    ("What is the airspeed of an unladen swallow in miles/hr", "12"),
    ("What is the capital of Texas", "Austin"),
    ("The Last Supper was painted by which artist", "Da Vinci")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")