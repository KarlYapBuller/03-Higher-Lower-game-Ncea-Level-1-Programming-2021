#Get and Check User input

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

#Main Routine

lowest = integer_check("Low Number: ")
highest = integer_check("High Number: ", lowest + 1)
rounds = integer_check("Rounds: ", 1)
guess = integer_check("Guess: ", lowest, highest)





