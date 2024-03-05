import random
import os
import art


def compare(guess):
    global attempts
    global loop

    guess = int(guess)
    
    if attempts - 1 == 0:
        loop = False
        print("You've run out of guesses, you lose.")
    elif chosen_number == guess:
        loop = False
        print(f"You got it! The answer was {chosen_number}, while haveing {attempts} attempts left.")
    elif chosen_number > guess:
        attempts -= 1
        print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
    elif chosen_number < guess:
        attempts -= 1
        print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")



play_again = True
while play_again == True:
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    chosen_number = random.randint(1,100)
    accepted = True
    while accepted == True:

        difficulty = input("Choose a difficulty. \nType 'easy' or 'hard': " ).lower()
        attempts = 0

        if difficulty == 'easy':
            attempts = 10
        elif difficulty == 'hard':
            attempts = 5

        if difficulty == "easy" or difficulty == "hard":
            loop = True
            while loop == True:
                guess = input("Make a guess: ")

                if guess.isnumeric() and 0 <= int(guess) <= 100:
                    compare(guess)
                else:
                    print("Please enter a number which is with in 0 to 100.")
            accepted = False
        else:
            os.system('cls')
            print(art.logo)
            print("Welcome to the Number Guessing Game!")
            print("I'm thinking of a number between 1 and 100")

    again = input("Do you want to play again, 'yes' or 'no': ")
    if again == 'yes':
        os.system('cls')
        play_again = True
    else:
        play_again = False
        
input("Tap Enter to Exit!")