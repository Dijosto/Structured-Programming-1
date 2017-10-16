from random import *
hangmanascii = ['''
 
 
  +---+
  |   |
      |
      |
      |
 =========''', '''
  +---+
  |   |
  0   |
      |
      |
 =========''', '''
  +---+
  |   |
  0   |
  |   |
      |
 =========''', '''
  +---+
  |   |
  0   |
 /|   |
      |
 =========''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
 =========''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
 =========''', '''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
 =========''']
words = ["Kali","Linux","Ubuntu","Java","Daniel"]
def randomWord(wordlist):
    #gets one of the words
    wordIndex = random.randint(0, len(wordlist) -1)
    return wordList[wordIndex]
def displayBoard(hangmanascii, missedLetters, correctLetters, secretWord):
    print(hangmanascii[len(missedLetters)])
    print()

    print('False letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blank = '_' * len(secretWord)

    for i in range(len(secretWord)): #puts the correct words in the blanks
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for letter in blanks: # puts the correct words in
        print(letter, end=' ')
    print()
def getGuess(guessed):
    #returns guessed letters
    while True:
        print('Guess a letter.')
        guess = input() #input for users letter
        guess = guess.lower()
        if len(guess) != 1:
            print('Only single letters.')
        elif guess in guessed:
            print('You guessed this letter already, try again!')
        elif guess not in alphabet:
            print('You must enter a letter')
        else:
            return guess
def playAgain():
    #if the player wants to play again
    print('Do you want to play again? (y/n)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

white True:
    displayBoard(hangmanascii, missedLetters, correctLetters, secretWord)
