"""
# MasterMind
"""
MAX_TURNS = 10
CORRECT_COLOR = "#"
CORRECT_POSITION = "$"
CHEAT = True  # helpful when debugging!
history = []

import random
#rules of the game
def printRules():
  greeting = "Welcome to Mastermind!"
  greetingCenter = greeting.center(34,'-')
  print(greetingCenter)
  print('The colors in the game are red (r), orange (o), yellow (y), green (g), blue (b) and purple (p)')
  print("'#' represents the correct color peg but in the incorrect position")
  print("'$' represents the correct color peg in the correct color position")

def setCode(repeat):
  # repeats for each colored peg in the code:
  # selects a random color
  # add it to the answer
  # if no repeats, removes that color from available colors
  code = []
  if repeat=='Y' or repeat == 'y':
    for i in range(pegs):
      color1 = random.choice(colors)
      code.append(color1)
  elif repeat=='N' or repeat == 'n':
    for i in range(pegs):
      color1 = random.choice(colors)
      code.append(color1)
      colors.remove(color1)
  return code
  pass


def getResponse(guess, code1):
  output_string = ''
  guess1 = guess.split()
  response = ''
  for i in range(len(guess1)):
    if guess1[i]==code1[i]:
      response += '$ '
    elif guess1[i] in code1:
      response += '# '
    elif guess1[i] not in code1:
      response += ''
  response = response.split(' ')
  response = sorted(response)
  for i in response:
    if not i == '':
      output_string += i
  return output_string
  # checks to see if each letter of the guess is the right color or in the right place
  # and calculates the response





def showHistory(guesses, history):
    history += turns, guess, response
    return history

  # print results of each turn in the guesses list



## main starts here
colors = ['R', 'O', 'Y', 'G', 'B', 'P',]
answer = ''
guessoutput = ""

# print opening greetings
printRules()

# get inputs(repeats allowed, and how many pegs?)
repeats = input("Can the colors repeat? Type 'Y' for yes or 'N' for no: ")
pegs = int(input('Choose how many pegs(4, 5, or 6): '))


# set the code with or without repeats
code = setCode(repeats)
#shows the correct answer
if CHEAT:
  print("Shhhhh! Here's the code: ", code)

print(f"You have {MAX_TURNS} turns to guess the code!")

turns = 0
win = False
guesses = []
gameOver = False


while not gameOver:

  turns += 1
  # gets the guess from the user
  print("Colors are roygbp. ", end = '')
  guess = input("Enter your guess with a space between each color(r b g y for red blue green yellow): ")
  guess = guess.upper()

  # calculate the response
  response = getResponse(guess, code)


#shows previous guesses
  history = showHistory(guesses, history)
  print("Guesses:")
  for i in range(0, len(history), 3):
    print(history[i:i+3])


  # checks to see if the game is over
  if turns == MAX_TURNS or guess.split() == code:
    if guess.split() == code:
      win = True
    else:
      win = False

    if win:
      print(f"Congrats you won in {turns} guesses!")
    else:
      print("Sorry looks like you didn't crack the code!")
      print(f"The correct answer is {code}")


    gameOver = True

