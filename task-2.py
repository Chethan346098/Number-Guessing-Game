import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            
            # Check if guess is valid
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Please enter a valid number.")
    
    # If all attempts are used
    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    while play_again == 'yes':
        number_guessing_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
    print("\nThanks for playing! Goodbye!")