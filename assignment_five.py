#Charlotte
#1/5/23
#This program is a guessing game


import random



def get_number():
    '''
    This function sets the random number for the user to guess
    :return: Random number of type interger
    '''
    number = random.randint(1,100)
    return number

def introduction():
    '''
    This function introduces the game and gets the users name
    :return: user's name of type string
    '''
    print("Hi queen! This is a guessing game. You guess a number between 1-100 and ill tell you if its too high or too low, until you get it right.")
    user_name = input("What is your name?")
    return user_name






def get_guess():
    '''
    This function gets the user to enter their guess
    :return: The users guess type interger
    '''
    guess1 = input("Enter your guess")
    x = 0
    x = x + 1


    return guess1

def main():
    '''
    This function plays the game and tells the user if their guess is too high or low
    '''
    introduction()                                  # Calls the introduction function
    for x in range(3):                              # Loops 3 times
        print("New game")                           # prints "new game"
        random_number = get_number()                # calls random number and assighns it to a name
        average = 0
        while True:
            guess = int(get_guess())                # Calls get guess function and assighns it to a name + maks it a int

            if guess > random_number:
                average = average + 1
                print("Your guess is too high")     # tells the user their guess is too high
            if guess < random_number:
                average = average + 1
                print("Your guess is too low")
            if guess == random_number:
                print("Correct!")
                print("you guess", average, " times wrong")
                break

main()
