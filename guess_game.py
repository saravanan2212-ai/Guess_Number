import random

while True:
    number_to_guess = random.randint(1, 100)
    attempts = 0
    user_guess = 0

    print("\nWelcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it as quickly as you can.")

    while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Higher! Try again.")
        elif user_guess > number_to_guess:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
