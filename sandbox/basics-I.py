import random


numMin = 1
numMax = 100

# Get a Random number between min and Max
randomNumber = random.randrange(numMin, numMax)

# Prompt User to pick a number
prompt = "Pick a number between {} and {} " .format(numMin, numMax)

randomRange = input(prompt)
guess = int(randomRange)


if guess == randomNumber:
    print("Correct! The number was {}" .format(randomNumber))
if guess != randomNumber:
    print("Ahh Dang so close! Lets try again?")

    secondGuess = input("Pick another number (thats not) {} " .format(guess))

    if secondGuess == randomNumber:
        print("holy shit you did it!")
    elif secondGuess == guess:
        print("Shit you dumb!")
    else:
        print("Ahh Dang sooo close! Last try?")

        thirdGuess = input("Pick another number (thats not) {} or {}" .format(guess, secondGuess))

        if thirdGuess == randomNumber:
            print("Holy shit you did it!")
        else:
            print("You are worthless")








# Testing
# print(str(randomRange))
# print(randomNumber)
# print("Correct! The number was {}" .format(randomNumber))
# print("Ahh Dang! The correct number was {}!" .format(randomNumber))
