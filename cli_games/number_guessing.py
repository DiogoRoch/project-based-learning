import random

random_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is? You have 10 attempts.")

def is_valid_input(user_input):
    """Check if the input is a valid integer."""
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def evaluate_guess(guess, random_number):
    """Evaluate the user's guess against the random number."""

    if not is_valid_input(guess):
        return (0, "Invalid input! Please enter a number between 1 and 100.")

    if guess < random_number:
        return  (0, "Too Low!")
    elif guess > random_number:
        return (0, "Too High!")
    else:
        return (1, "Congratulations! You've guessed the number!")

while attempts < 10:
    guess = input(f"Attempt {attempts + 1}: Enter your guess: ")
    attempts += 1
    result, message = evaluate_guess(int(guess), random_number)
    print(message)
    if result == 1:
        break
if attempts == 10:
    print(f"Sorry! You've used all your attempts. The number was {random_number}.")