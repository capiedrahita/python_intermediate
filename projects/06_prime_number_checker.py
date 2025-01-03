
# Prime Number Checker
# This program checks if a given number is prime.

try:
    # Step 1: Ask the user for a number
    num = int(input("Enter a number to check if it's prime: "))
    if num <= 1:
        print("Numbers less than or equal to 1 are not prime.")
    else:
        # Step 2: Check for factors
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        # Step 3: Display the result
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
