
# Math Quiz
# This program generates random math problems for the user to solve.

import random

# Step 1: Define the number of questions
num_questions = 5
score = 0

print("Welcome to the Math Quiz!")
print(f"You will be given {num_questions} questions. Try your best!")

# Step 2: Generate and ask questions
for i in range(1, num_questions + 1):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    correct_answer = eval(f"{num1} {operation} {num2}")

    # Ask the question
    try:
        user_answer = float(input(f"Question {i}: {num1} {operation} {num2} = "))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    except ValueError:
        print("Invalid input. Moving to the next question.")

# Step 3: Display the final score
print(f"You got {score}/{num_questions} correct. Well done!")
