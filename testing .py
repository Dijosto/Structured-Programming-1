from tkinter import *




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
""")

def main():
    words = ["hangman", "
                 ]
    chosen_word = random.choice(words).lower()
    player_guess = None
    guessed_letters = []
    word_guessed =[]
    for letter in chosed_word:
        word_guessed.append("-") # creates blank
    joined_word = None
    attempts = len(HANGMAN) - 1

    while (attempts != 0 and "-" in word_guessed):
        Text(text='hey').grid(column=1,row=6)


def select():
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
result_set = StringVar()
#Labels 
Label(mainframe, text='ASCII ( HANG MAN )',bg='blue').grid(column=1, row =1, sticky = E)
Label(mainframe, text=HANGMAN,bg='blue').grid(column=1, row =2, sticky = W)
#Hangman ascii ^
#select button
Button(mainframe, text="Select", command = select).grid(column = 1, row = 3, sticky = W)

#All of the letters 
Label(mainframe, text='Guess what letter',bg='blue').grid(column=1, row =5, sticky= W)
Radiobutton(mainframe, text ='A', variable = guessed, value = 'A',bg='gray').grid(column=2, row=6, sticky=W)
Radiobutton(mainframe, text ='B', variable = guessed, value = 'B',bg='gray').grid(column=3, row=6, sticky=W)
Radiobutton(mainframe, text ='C', variable = guessed, value = 'C',bg='gray').grid(column=4, row=6, sticky=W)
Radiobutton(mainframe, text ='D', variable = guessed, value = 'D',bg='gray').grid(column=5, row=6, sticky=W)
Radiobutton(mainframe, text ='E', variable = guessed, value = 'E',bg='gray').grid(column=6, row=6, sticky=W)
Radiobutton(mainframe, text ='F', variable = guessed, value = 'F',bg='gray').grid(column=7, row=6, sticky=W)
Radiobutton(mainframe, text ='G', variable = guessed, value = 'G',bg='gray').grid(column=8, row=6, sticky=W)
Radiobutton(mainframe, text ='H', variable = guessed, value = 'H',bg='gray').grid(column=9, row=6, sticky=W)
Radiobutton(mainframe, text ='I', variable = guessed, value = 'I',bg='gray').grid(column=10, row=6, sticky=W)
Radiobutton(mainframe, text ='J', variable = guessed, value = 'J',bg='gray').grid(column=11, row=6, sticky=W)
Radiobutton(mainframe, text ='K', variable = guessed, value = 'K',bg='gray').grid(column=12, row=6, sticky=W)
Radiobutton(mainframe, text ='L', variable = guessed, value = 'L',bg='gray').grid(column=13, row=6, sticky=W)
Radiobutton(mainframe, text ='M', variable = guessed, value = 'M',bg='gray').grid(column=14, row=6, sticky=W)
Radiobutton(mainframe, text ='N', variable = guessed, value = 'N',bg='gray').grid(column=2, row=7, sticky=W)
Radiobutton(mainframe, text ='O', variable = guessed, value = 'O',bg='gray').grid(column=3, row=7, sticky=W)
Radiobutton(mainframe, text ='P', variable = guessed, value = 'P',bg='gray').grid(column=4, row=7, sticky=W)
Radiobutton(mainframe, text ='Q', variable = guessed, value = 'Q',bg='gray').grid(column=5, row=7, sticky=W)
Radiobutton(mainframe, text ='R', variable = guessed, value = 'R',bg='gray').grid(column=6, row=7, sticky=W)
Radiobutton(mainframe, text ='S', variable = guessed, value = 'S',bg='gray').grid(column=7, row=7, sticky=W)
Radiobutton(mainframe, text ='T', variable = guessed, value = 'T',bg='gray').grid(column=8, row=7, sticky=W)
Radiobutton(mainframe, text ='U', variable = guessed, value = 'U',bg='gray').grid(column=9, row=7, sticky=W)
Radiobutton(mainframe, text ='V', variable = guessed, value = 'V',bg='gray').grid(column=10, row=7, sticky=W)
Radiobutton(mainframe, text ='W', variable = guessed, value = 'W',bg='gray').grid(column=11, row=7, sticky=W)
Radiobutton(mainframe, text ='X', variable = guessed, value = 'X',bg='gray').grid(column=12, row=7, sticky=W)
Radiobutton(mainframe, text ='Y', variable = guessed, value = 'Y',bg='gray').grid(column=13, row=7, sticky=W)
Radiobutton(mainframe, text ='Z', variable = guessed, value = 'Z',bg='gray').grid(column=14, row=7, sticky=W)



mainloop()
