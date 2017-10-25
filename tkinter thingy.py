from tkinter import *
import os 
from random import randint
import time
master = Tk()

def start():
    os.system('games boiiiaa.py')
    sys.exit(Screen)
def callback():
    print("The game has started!")
    start()




Screen = Frame(master, height=500, width=400)
f = Frame(master, height=100, width=100)
f.pack_propagate(0) # don't shrink
f.pack()
Screen.pack()
f.place(relx=0.5, rely=0.5, anchor=CENTER)
b = Button(f, text="Start!", command=callback)

b.pack(fill=BOTH, expand=1)
mainloop()
