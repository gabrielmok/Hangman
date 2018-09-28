import random
HANGMANSTATES = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'silicon element icicle popsicle sandwich convert faxing slider angular' .split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(HANGMANSTATES, missedLetters, correctLetters, secretWord):
    print (HANGMANSTATES[len(missedLetters)])  #prints current picture
    print ()
    print ('Missed Letters: ', end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    blanks = '_' * len(secretWord)  #printing blank spaces

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print (letter, end=" ")
    print()

def userguess(alreadyguessed):
    while True:
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyguessed:
            print("You have already guessed this letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("This isn't a letter.. -.-")
        else:
            return guess

def playAgain():
    print("Do you want to play again?: ")
    return input().lower().startswith('y')
        
#main program
    
print("Hangman")
secretWord = getRandomWord(words)
missedLetters = ''
correctLetters = ''	
gameisdone = False

while True:
    displayBoard (HANGMANSTATES, missedLetters, correctLetters, secretWord)
    guess = userguess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundallletters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundallletters = False
                break
        if foundallletters:
            print("You have correctly guessed the word " + secretWord)
            gameisdone = True

    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANSTATES) -1:
            displayBoard(HANGMANSTATES, missedLetters, correctLetters, secretWord)
            print ("Sorry, you have lost the game. The word was " + secretWord)
            gameisdone = True
    if gameisdone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameisdone = False
            secretWord = getRandomWord(words)
        else:
            break
