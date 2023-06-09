import random  # We need the 'random' library to generate random numbers.

def guess_the_number():
    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    # Initialize the number of attempts.
    attempts = 0

    # Continue looping until the user guesses the correct number.
    while True:
        # Prompt the user for their guess.
        guess = input("Enter your guess: ")

        # Try to convert the user's input to an integer.
        try:
            guess = int(guess)
        except ValueError:
            # If the input is not a number, print an error message and ask again.
            print("That's not a valid number! Please enter a number between 1 and 100.")
            continue

        # Increment the number of attempts.
        attempts += 1

        # Check if the user's guess is correct, too high, or too low.
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Start the game if script is being run directly, not being imported as a module
if __name__ == "__main__":
    guess_the_number()
