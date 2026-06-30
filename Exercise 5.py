# Exercise 1
'''
The output will be:
20
10
'''

'''

# Exercise 2

def calculate_grade(score):
    if score >= 90:
          return "A"
    elif score >= 80:
          return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
'''       
'''
# Exercise 3

def average(*numbers):
    if not numbers:
        return 0
        
    return sum(numbers) / len(numbers)


print("The average for numbers(10,20,30) is: ", average(10, 20, 30))
'''
'''
#Exercise 4
def build_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile
    
    
user_1 = build_profile("Nada", age=29, city="Gaza")

print("Profile 1:", user_1)
'''
# Exercise 5
questions: list[dict] = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "define", "D": "function"},
        "answer": "B"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3.0", "C": "3", "D": "4"},
        "answer": "C"
    },
    {
        "question": "Which of these is a falsy value in Python?",
        "options": {"A": '"False"', "B": "1", "C": "0", "D": "-1"},
        "answer": "C"
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": {
            "A": "Skips to the next iteration",
            "B": "Restarts the loop from the beginning",
            "C": "Exits the loop immediately",
            "D": "Pauses the loop for 1 second"
        },
        "answer": "C"
    },
    {
        "question": "What is the correct way to call a function named 'greet' with argument 'Alice'?",
        "options": {"A": "greet['Alice']", "B": "call greet('Alice')", "C": "greet.Alice", "D": "greet('Alice')"},
        "answer": "D"
    },
]




def check_answer(user_answer: str, correct_answer: str) -> bool:
    #Compare user input with the correct answer case-insensitively.
    return user_answer.strip().upper() == correct_answer.strip().upper()


def calculate_percentage(score: int, total: int) -> float:
    #Compute the percentage score, preventing division by zero.
    if total <= 0:
        return 0.0
    return (score / total) * 100


def get_grade_report(percentage: float) -> tuple[str, str]:
    #Determine the letter grade and motivation message based on percentage score.
    if percentage >= 90:
        return "A", "🏆 Outstanding! You really know your Python!"
    if percentage >= 75:
        return "B", "🎉 Great job! Solid Python knowledge."
    if percentage >= 60:
        return "C", "✅ Good effort. Keep practising!"
    if percentage >= 40:
        return "D", "📖 Keep studying — you're getting there."
    return "F", "💪 Review the lessons and try again!"



def show_welcome(total_questions: int) -> None:
    """Print the welcome banner and rules."""
    print("=" * 45)
    print("       🐍 PYTHON KNOWLEDGE QUIZ 🐍")
    print("=" * 45)
    print(f"  Questions : {total_questions}")
    print("  Options   : A, B, C, or D")
    print("  Type 'quit' at any time to exit")
    print("=" * 45)
    print()


def display_question(number: int, total: int, question_data: dict) -> None:
    #Display a single question with its options formatted.
    print(f"Question {number}/{total}")
    print("-" * 40)
    print(f"  {question_data['question']}")
    print()
    options = question_data["options"]
    if isinstance(options, dict):
        for key, value in options.items():
            print(f"  {key}) {value}")
    print()


def get_user_input() -> str:
    #Prompt the user until a valid choice or 'quit' command is entered.
    valid_choices = ["a", "b", "c", "d", "quit"]
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer in valid_choices:
            return answer
        print("  ⚠️  Please enter A, B, C, D, or 'quit'.")


def show_results(score: int, total: int, quit_early: bool) -> None:
    #Format and print the final scoreboard using calculation helpers.
    percentage = calculate_percentage(score, total)
    grade, message = get_grade_report(percentage)

    print()
    print("=" * 45)
    if quit_early:
        print("  You quit the quiz early.")
    print("       📊 YOUR RESULTS")
    print("=" * 45)
    print(f"  Score      : {score} / {total}")
    print(f"  Percentage : {percentage:.1f}%")
    print(f"  Grade      : {grade}")
    print("-" * 45)
    print(f"  {message}")
    print("=" * 45)


# ── Main Game Loop ────────────────────────────────────────────────

def run_quiz(quiz_questions: list[dict]) -> None:
    # Organizing the running procedure
    total_questions = len(quiz_questions)
    show_welcome(total_questions)

    score = 0
    quit_early = False
    questions_answered = 0

    for i, question_data in enumerate(quiz_questions, start=1):
        display_question(i, total_questions, question_data)
        user_answer = get_user_input()

        if user_answer == "quit":
            quit_early = True
            break

        correct_key = str(question_data["answer"])
        if check_answer(user_answer, correct_key):
            print("  ✅ Correct!\n")
            score += 1
        else:
            options = question_data["options"]
            correct_value = options[correct_key] if isinstance(options, dict) else ""
            print(f"  ❌ Wrong. The correct answer was {correct_key}) {correct_value}\n")

        questions_answered = i

    final_total = questions_answered if quit_early else total_questions
    show_results(score, final_total, quit_early)


# Starting point

if __name__ == "__main__":
    run_quiz(questions)
