#Higher Lower game Secret Number

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
            print("Please enter an integer")
            continue

lowest = integer_check("Low Number: ")
highest = integer_check("High Number: ", lowest + 1)

number_range = highest - lowest + 1
max_raw = math.log2(number_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

secret = random.randint(lowest, highest)

print(secret)
