# Quiz 4.  Put questions and answers into a dictionary, to
# include answer options.
# Allow the user to select the correct answer by its label.
# Name: Micah French
# Date: October 3, 2025

# Quiz questions. For each question list the possible answers, with the first answer being the correct one.
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "24", "36", "48"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "Waco"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives, 1):
        print(f" {label}. {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label - 1]
    
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")