"""
# MasterMind Starter File
"""
MAX_TURNS = 999
CORRECT_COLOR = "??"
CORRECT_POSITION = "??"
CHEAT = True  # helpful when debugging!
import random

def printRules():
    print("Welcome to Mastermind...")

def setCode(repeat):
    code = ""
    # repeat for each colored peg in the code:
    # select a random color
    # add it to the answer
    # if no repeats, remove that color from available colors
    return code
    pass


def getResponse(guess):
    # check if each letter of the guess is the right color or in the right place
    # and calculate the response
    return response
    pass


def showHistory(guesses):
    print("Guesses:")
    # print results of each turn in the guesses list



## main starts here
colors = ['r','y','g']  # add the colors
answer = ""
guessoutput = ""

# print opening greetings
printRules()

# get inputs(repeats allowed?)
repeats = input("...")

# set the code with or without repeats
code = setCode(repeats)

if CHEAT:
    print("Shhhhh! Here's the code: ", code)

print(f"You have {MAX_TURNS} turns to guess the code!")

turns = 0
win = False
guesses = []
gameOver = False

while not gameOver:

    # increase number of turns
    # get the guess from the user
    guess = input("....")

    # calculate the response
    response = getResponse(guess)
    guess_output = f"{turns:>2}\t{guess}\t{response}"
    # add this guess and response to the list of guesses
    # print  guesses

    showHistory(guesses)

    # check game is over  (check for win or lose conditions)
    if True:  # replace with the correct condition
        gameOver = True


if win:
    print("Congrats you won in", turns, "guesses!")
else:
    print("Sorry looks like you didn't crack the code!")
    print(f"The correct answer is {answer}")
