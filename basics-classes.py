import random

numMin = 1
numMax = 100
#
randomNumber = random.randrange(numMin, numMax)

guess = 40
correct = 41


class question:
    def __init__(self, attempt, guess):
        self.attempt = int(attempt)
        self.guess = int(guess)

        if guess == correct:
            print("CORRECT! :) ")
        elif guess != correct:
            print("WRONG! Try again?")






def main():
    first = question(1, 40)
    # print(correct)





if __name__ == "__main__":
    main()





#
# first.set_guessAmount(667)
# input(first.set_guessAmount)
# def set_guessAmount(self, guessAmount):
#     guessEntry = input("Pick a number between {} and {} " .format(numMin, numMax))
# guess_type = "Rando"
# guess_color = "pink"
# firstGuess = guessEntry(452)
#
#
#
# print(firstGuess.guessAmount)


        # animal_type = "fish"
        # location = "ocean"
        # followers = 5
