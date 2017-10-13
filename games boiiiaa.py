#!usr/bin/env python3

from random import randint
import time
rock = 1
paper = 2
scissors = 3

names = {rock: "rock", paper: "paper", scissors: "scissors"}

rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0


user =  input("Enter your name here: ")    
def start():
    print("Hey lets play some rock paper scissors!")
    
    print("Hello {}! Welcome to the great and wonderful game of Rock, Paper, and Scissors.".format(user))
    while game():
            pass
    scores()
def game():
    player = move()
    computer = randint(1,3)
    result(player, computer)
    return play_again()
def move():
    while True:
            print
            player = input("Rock = 1 Paper = 2 Scissors = 3 Make a move: ")
            try:
                    player = int(player)
                    if player in (1,2,3,4):
                            return player
            except ValueError:
                    pass
            print("Please enter 1, 2, or 3.")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer used {}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
            print("You guys tied")
    else:
            if rules[player] == computer:
                    print("{} has won the game.".format(user))
                    player_score += 1
            else:
                    print("The computer has won.")
                    computer_score += 1
def play_again():
    answer = input("Would you like to paly again? y/n: ")
    if answer in ("y", "Y", "Yes", "yea", "Yea", "yeah", "Yeah"):
            return answer
    else:
            print("Thanks for playing!")
        
                        
    
    
