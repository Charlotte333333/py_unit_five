
import random

def get_number():
    """This function sets the random number for the user to guess"""
    number = random.randint(1,100)
    return number

def introduction():
    """This function introduces the game and gets the users name"""
    print("Hi queen! This is a guessing game. You guess a number between 1-100 and ill tell you if its too high or too low, until you get it right.")
    user_name = input("What is your name?")
    return user_name






def get_guess():
    """This function gets the user to enter their guess"""
    guess1 = input("Enter your guess")
    return guess1

def main():
    """This function plays the game"""
    introduction()
    for x in range(3):
        print("New game")
        random_number = get_number()
        while True:
            guess = int(get_guess())
            if guess > random_number:
                print("Your guess is too high")
            if guess < random_number:
                print("Your guess is too low")
            if guess == random_number:
                print("Correct!")
                break

main()
