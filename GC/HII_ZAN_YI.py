import random

player1=0
player2=0
print("welcome to rock paper scissors. finish to end.")
manual = input("manual or auto? (y for manual n for auto)").lower()
in1=input("player1: rock, paper, or scissors? ").lower()
lst=["rock", "paper", "scissors"]
if manual=="n":
    in2 = lst[random.randint(0,2)]
    print(f"player 2 choose {in2}")
else:
    in2=input("player2: rock, paper, or scissors? ").lower()
    
if in2 not in ["rock", "paper", "scissors"] or in1 not in ["rock", "paper", "scissors"]:
    print("invalid input!")
x=0
while in1 != "finish" or in2!= "finish":
    if in1=="rock":
        if in2 == "paper":
            print("player 2 wins! +1")
            player2+=1
        elif in2 == "scissors":
            print("player 1 wins! +1")
            player1+=1
        else:
            print("draw!")
    if in1 == "paper":
        if in2 == "rock":
            print("player 1 wins! +1")
            player1 +=1
        elif in2 == "scissors":
            print("player 2 wins! +1")
            player2+=1
        else:
            print("draw!")
    if in1 == "scissors":
        if in2 == "rock":
            print("player 2 wins! +1")
            player2 +=1
        elif in2 == "paper":
            print("player 1 wins! +1")
            player1+=1
        else:
            print("draw!")
    print(f"-------------------New Round (Round {x})----------------------")
    in1=input("player1: rock, paper, or scissors?").lower()
    if in1 == "finish":
        break
    if manual=="n":
        in2 = lst[random.randint(0,2)]
        print(f"player 2 choose {in2}")
    else:
        in2=input("player2: rock, paper, or scissors? ").lower()
    if in2 == "finish":
        break
    if in2 not in ["rock", "paper", "scissors"] or in1 not in ["rock", "paper", "scissors"]:
        print("invalid input!")
    x+=1
print(f"score of player 1: {player1}. \nscore of player 2: {player2}.")

if player1>player2:
    print("player 1 wins!")
elif player1<player2:
    print("player 2 wins!")
else:
    print("draw!")