from tkinter import *
import random



HANGMAN = (
"""
-------
|             |
              |
              |
              |
              |
              |
              |
              |
-----------
""","""
-------
|             |
0             |
              |
              |
              |
              |
              |
              |
-----------
""","""
-------
|             |
0             |
|             |
              |
              |
              |
              |
              |
-----------
""","""
-------
|             |
0             |
|\            |
              |
              |
              |
              |
              |
-----------
""","""
-------
 |            |
 0            |
/|\           |
              |
              |
              |
              |
              |
-----------
""","""
-------
 |            |
 0            |
/|\           |
/             |
              |
              |
              |
              |
-----------
""","""
-------
 |            |
 0           |
/|\          |
/ \          |
              |
              |
              |
              |
-----------
""")

HANGMANSS = HANGMAN[0]eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
words = ["hangman","word","kittens"]
chosenWord = random.choice(words)
playing = True
def select():
    guessedLetter = guessed.get()
    
    
    guessed_letters = []
    word_guessed = []
    for letter in guessedLetter(range(n))
        guessed_letters.append(letter)
    
    print(guessed_letters)    
    if guessedLetter in chosenWord:
            
            print("Correct")ee
    else:e
            
            print("incorrect")
    Label(mainframe, text=guessedLetter)
    return




#start of gui
root = Tk()
root.title ('Hangman in TKinter')

mainframe = Frame(root, padx = '100')
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)

mainframe.configure(bg='gray')
guessed = StringVar()
#Labels 
Label(mainframe, text='ASCII ( HANG MAN )',bg='blue').grid(column=1, row =1, sticky = E)
Ascii = Label(mainframe, text=HANGMAN[0],bg='blue').grid(column=1, row =2, sticky = W)
#Hangman ascii ^
#select button
Button(mainframe, text="Select", command = select).grid(column = 1, row = 3, sticky = W)


#All of the letters 
Label(mainframe, text="Select your choice",bg='gray').grid(column=1, row =5, sticky= W)
Radiobutton(mainframe, text ='A', variable = guessed, value = 'a',bg='gray').grid(column=2, row=6, sticky=W)
Radiobutton(mainframe, text ='B', variable = guessed, value = 'b',bg='gray').grid(column=3, row=6, sticky=W)
Radiobutton(mainframe, text ='C', variable = guessed, value = 'c',bg='gray').grid(column=4, row=6, sticky=W)
Radiobutton(mainframe, text ='D', variable = guessed, value = 'd',bg='gray').grid(column=5, row=6, sticky=W)
Radiobutton(mainframe, text ='E', variable = guessed, value = 'e',bg='gray').grid(column=6, row=6, sticky=W)
Radiobutton(mainframe, text ='F', variable = guessed, value = 'f',bg='gray').grid(column=7, row=6, sticky=W)
Radiobutton(mainframe, text ='G', variable = guessed, value = 'g',bg='gray').grid(column=8, row=6, sticky=W)
Radiobutton(mainframe, text ='H', variable = guessed, value = 'h',bg='gray').grid(column=9, row=6, sticky=W)
Radiobutton(mainframe, text ='I', variable = guessed, value = 'i',bg='gray').grid(column=10, row=6, sticky=W)
Radiobutton(mainframe, text ='J', variable = guessed, value = 'j',bg='gray').grid(column=11, row=6, sticky=W)
Radiobutton(mainframe, text ='K', variable = guessed, value = 'k',bg='gray').grid(column=12, row=6, sticky=W)
Radiobutton(mainframe, text ='L', variable = guessed, value = 'l',bg='gray').grid(column=13, row=6, sticky=W)
Radiobutton(mainframe, text ='M', variable = guessed, value = 'm',bg='gray').grid(column=14, row=6, sticky=W)
Radiobutton(mainframe, text ='N', variable = guessed, value = 'n',bg='gray').grid(column=2, row=7, sticky=W)
Radiobutton(mainframe, text ='O', variable = guessed, value = 'o',bg='gray').grid(column=3, row=7, sticky=W)
Radiobutton(mainframe, text ='P', variable = guessed, value = 'p',bg='gray').grid(column=4, row=7, sticky=W)
Radiobutton(mainframe, text ='Q', variable = guessed, value = 'q',bg='gray').grid(column=5, row=7, sticky=W)
Radiobutton(mainframe, text ='R', variable = guessed, value = 'r',bg='gray').grid(column=6, row=7, sticky=W)
Radiobutton(mainframe, text ='S', variable = guessed, value = 's',bg='gray').grid(column=7, row=7, sticky=W)
Radiobutton(mainframe, text ='T', variable = guessed, value = 't',bg='gray').grid(column=8, row=7, sticky=W)
Radiobutton(mainframe, text ='U', variable = guessed, value = 'u',bg='gray').grid(column=9, row=7, sticky=W)
Radiobutton(mainframe, text ='V', variable = guessed, value = 'v',bg='gray').grid(column=10, row=7, sticky=W)
Radiobutton(mainframe, text ='W', variable = guessed, value = 'w',bg='gray').grid(column=11, row=7, sticky=W)
Radiobutton(mainframe, text ='X', variable = guessed, value = 'x',bg='gray').grid(column=12, row=7, sticky=W)
Radiobutton(mainframe, text ='Y', variable = guessed, value = 'y',bg='gray').grid(column=13, row=7, sticky=W)
Radiobutton(mainframe, text ='Z', variable = guessed, value = 'z',bg='gray').grid(column=14, row=7, sticky=W)



mainloop()
