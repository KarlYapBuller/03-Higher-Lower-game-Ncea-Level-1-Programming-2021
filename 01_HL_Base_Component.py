#Higher Lower game

import random
import math

#Number Checking Function goes here

def integer_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        except ValueError:
            print("Please enter an integer. You still have {} guesses left.".format(guesses_left))
            continue

lowest = integer_check("Low Number: ")
highest = integer_check("High Number: ", lowest + 1)

secret = random.randint(lowest, highest)

print(secret)

number_range = highest - lowest + 1
max_raw = math.log2(number_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

guesses_allowed = max_guesses

already_guessed = []
guesses_left = guesses_allowed
number_won = 0

guess = ""

while guess != secret and guesses_left >= 1:
    #Replace this with the 02_HL_Get_and_Check_User_Choice_v1.py
    guess = integer_check("Guess: ")

    #Check that the guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < secret:
            print("Too low, try a higher number. Guesses left {}.".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number. Guesses left {}.".format(guesses_left))

    else:
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print("Amazing. You have got it")
    else:
        print("Well Done. You have got it")
