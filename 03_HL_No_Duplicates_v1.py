#No Duplicates

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
number_won = 0

guess = ""

while guess != secret and guesses_left >= 1:
    #Replace this with the 02_HL_Get_and_Check_User_Choice_v1.py
    guess = int(input("Guess: "))

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





