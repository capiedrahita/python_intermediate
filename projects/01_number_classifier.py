
# Number Classifier
# This program classifies numbers as positive, negative, or zero.

try:
    # Step 1: Ask the user to input a number
    number = float(input("Enter a number: "))

    # Step 2: Classify the number
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    # Step 3: Check if the number is even or odd (if it's an integer)
    if number.is_integer():
        if int(number) % 2 == 0:
            print("It is an even number.")
        else:
            print("It is an odd number.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
