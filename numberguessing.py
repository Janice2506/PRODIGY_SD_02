import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while not guessed:
        # Prompt the user to input their guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()
