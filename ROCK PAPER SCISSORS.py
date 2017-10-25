

from tkinter import *

import random
import sys


def computerRandom():
    options = ["Rock","Paper","Scissors"]
    randomChoice = random.randint(0,2)
    computer_choice.set(options[randomChoice]) #added into the program
    return options[randomChoice]

def comparison(humanChoice, computerChoice):
    if humanChoice == computerChoice:
        return "Draw"
    if humanChoice == "Rock" and computerChoice == "Paper":
        return "Computer Wins"
    if humanChoice == "Paper" and computerChoice == "Scissors":
        return "Computer Wins"
    if humanChoice == "Scissors" and computerChoice == "Rock":
        return "Computer Wins"
    else: return "Human Wins"

def play():

    
    humanChoice = player_choice.get() 
    computerChoice =  computerRandom()

  
 
        
    result = comparison(humanChoice, computerChoice)

    if result == "Draw":
        result_set.set("Its a draw")
    elif result == "Computer Wins":
        result_set.set("Unlucky you lost!")
    else:  result_set.set("Well done you won!")
        

  
    


    


#all the gui
root = Tk()
root.title ('Rock Paper Scissors')

mainframe = Frame(root, padx = '100')
mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0,weight=1)

#Setting variables
player_choice = StringVar()
computer_choice = StringVar()
result_set = StringVar()



#layout for player
Label(mainframe, text='Player').grid(column=1, row = 1, sticky = W)
Radiobutton(mainframe, text ='Rock', variable = player_choice, value = 'Rock').grid(column=1, row=2, sticky=W)
Radiobutton(mainframe, text ='Paper', variable = player_choice, value = 'Paper').grid(column=1, row=3, sticky=W)
Radiobutton(mainframe, text ='Scissors', variable = player_choice, value = 'Scissors').grid(column=1, row=4, sticky=W)

#layout for computer
Label(mainframe, text='Computer').grid(column=3, row = 1, sticky = W)
Radiobutton(mainframe, text ='Rock', variable = computer_choice, value = 'Rock').grid(column=3, row=2, sticky=W)
Radiobutton(mainframe, text ='Paper', variable = computer_choice, value = 'Paper').grid(column=3, row=3, sticky=W)
Radiobutton(mainframe, text ='Scissors', variable = computer_choice, value = 'Scissors').grid(column=3, row=4, sticky=W)

#to play
Button(mainframe, text="Play", command = play).grid(column = 2, row = 2, sticky = W)

#the results
Label(mainframe, textvariable = result_set).grid(column = 1, row = 5, sticky =W, columnspan = 2)

root.mainloop()
