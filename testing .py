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



def select():
    return "Correct Guess"




#start of gui
root = Tk()
root.title ('Hangman in TKinter')

mainframe = Frame(root, padx = '100')
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)


guessed = StringVar()
result_set = StringVar()
#Labels 
Label(mainframe, text='ASCII ( HANG MAN )').grid(column=1, row =1, sticky = E)
Label(mainframe, text=HANGMAN).grid(column=1, row =2, sticky = W)
#Hangman ascii ^
#select button
Button(mainframe, text="Select", command = select).grid(column = 1, row = 3, sticky = W)

#All of the letters 
Label(mainframe, text='Guess what letter').grid(column=1, row =5, sticky= W)
Radiobutton(mainframe, text ='A', variable = guessed, value = 'A').grid(column=2, row=6, sticky=W)
Radiobutton(mainframe, text ='B', variable = guessed, value = 'B').grid(column=3, row=6, sticky=W)
Radiobutton(mainframe, text ='C', variable = guessed, value = 'C').grid(column=4, row=6, sticky=W)
Radiobutton(mainframe, text ='D', variable = guessed, value = 'D').grid(column=5, row=6, sticky=W)
Radiobutton(mainframe, text ='E', variable = guessed, value = 'E').grid(column=6, row=6, sticky=W)
Radiobutton(mainframe, text ='F', variable = guessed, value = 'F').grid(column=7, row=6, sticky=W)
Radiobutton(mainframe, text ='G', variable = guessed, value = 'G').grid(column=8, row=6, sticky=W)
Radiobutton(mainframe, text ='H', variable = guessed, value = 'H').grid(column=9, row=6, sticky=W)
Radiobutton(mainframe, text ='I', variable = guessed, value = 'I').grid(column=10, row=6, sticky=W)
Radiobutton(mainframe, text ='J', variable = guessed, value = 'J').grid(column=11, row=6, sticky=W)
Radiobutton(mainframe, text ='K', variable = guessed, value = 'K').grid(column=12, row=6, sticky=W)
Radiobutton(mainframe, text ='L', variable = guessed, value = 'L').grid(column=13, row=6, sticky=W)
Radiobutton(mainframe, text ='M', variable = guessed, value = 'M').grid(column=14, row=6, sticky=W)
Radiobutton(mainframe, text ='N', variable = guessed, value = 'N').grid(column=2, row=7, sticky=W)
Radiobutton(mainframe, text ='O', variable = guessed, value = 'O').grid(column=3, row=7, sticky=W)
Radiobutton(mainframe, text ='P', variable = guessed, value = 'P').grid(column=4, row=7, sticky=W)
Radiobutton(mainframe, text ='Q', variable = guessed, value = 'Q').grid(column=5, row=7, sticky=W)
Radiobutton(mainframe, text ='R', variable = guessed, value = 'R').grid(column=6, row=7, sticky=W)
Radiobutton(mainframe, text ='S', variable = guessed, value = 'S').grid(column=7, row=7, sticky=W)
Radiobutton(mainframe, text ='T', variable = guessed, value = 'T').grid(column=8, row=7, sticky=W)
Radiobutton(mainframe, text ='U', variable = guessed, value = 'U').grid(column=9, row=7, sticky=W)
Radiobutton(mainframe, text ='V', variable = guessed, value = 'V').grid(column=10, row=7, sticky=W)
Radiobutton(mainframe, text ='W', variable = guessed, value = 'W').grid(column=11, row=7, sticky=W)
Radiobutton(mainframe, text ='X', variable = guessed, value = 'X').grid(column=12, row=7, sticky=W)
Radiobutton(mainframe, text ='Y', variable = guessed, value = 'Y').grid(column=13, row=7, sticky=W)
Radiobutton(mainframe, text ='Z', variable = guessed, value = 'Z').grid(column=14, row=7, sticky=W)



mainloop()
