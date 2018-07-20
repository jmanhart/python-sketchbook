import random


numMin = 1
numMax = 1000000

# Get a Random number between min and Max
randomNumber = random.randrange(numMin, numMax)

# Prompt User to pick a number
prompt = "Pick a number between {} and {} " .format(numMin, numMax)

randomRange = input(prompt)
guess = int(randomRange)


if guess == randomNumber :
    print("Correct! The number was {}" .format(randomNumber))
else:
    print("Ahh Dang! The correct number was {}!" .format(randomNumber))





# Testing
# print(str(randomRange))
# print(randomNumber)
