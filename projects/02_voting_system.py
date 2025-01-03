
# Voting System
# This program determines if a person is eligible to vote based on their age and citizenship.

try:
    # Step 1: Ask for the user's age and citizenship status
    age = int(input("Enter your age: "))
    citizen = input("Are you a citizen? (yes/no): ").strip().lower()

    # Step 2: Determine voting eligibility
    if age >= 18 and citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a valid age.")
