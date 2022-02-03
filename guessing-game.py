import random

def guessNumber(range, tries):
  correctNumber = random.randint(1, range)

  gameWon = False
  triesRemaining = tries
  while not gameWon:
    answer = int(input("pick a number between 1 and {}: ".format(range) ))
    triesRemaining -= 1

    # check if the user got it right
    if answer == correctNumber:
      gameWon = True
    elif triesRemaining:
      if answer > correctNumber:
        print("too high! try again")
      else:
        print("too low! try again")

    if not gameWon:
      if triesRemaining == 1:
        print("last chance!")
      elif not triesRemaining:
        break

  if gameWon:
    print('Congrats! You got it in', tries - triesRemaining, 'tries')
  else:
    print('Better luck next time! The answer was', correctNumber)

def playGame():
  print('let\'s play a game!')
  selectedRange = int(input("How big a number should we guess?: "))
  selectedTries = int(input("How many tries do you want to have?: "))

  guessNumber(selectedRange, selectedTries)

playGame()
