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
            
