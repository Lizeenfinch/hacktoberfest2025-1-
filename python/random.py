import random

def guess_the_number():
    """
    A simple command-line game where the player guesses a random number.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize a variable to store the user's guess
    guess = 0
    
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess = int(input("Enter your guess: "))
            
            # Provide hints to the user
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
        
        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
