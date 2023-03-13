# Snake Water Gun is one of the famous two-player game played by many people. It is a hand game in which the player randomly chooses any of the three forms i.e. snake, water, and gun. Here, we are going to implement this game using python. 

# This python project is to build a game for a single player that plays with the computer 


import random

print("Welcome to Snake Water Gun game.....!")

n=int(input("Enter the number of rounds you want to play:"))

choices=['s','w','g']

rounds=1
comp_win=0
user_win=0

while(rounds<=n):
    print(f"Round:{rounds}\nSnake-'s'\nWater-'w'\nGun-'g'")

    try:
        player=input("Choose your option:")
    except EOFError as e:
        print(e)
    
    if player!='s' and player!='w' and player!='g':
        print("Invalid input,Please try again..!\n")
        continue

    computer=random.choice(choices)

    # Possible conditions
    if computer=='s':
        if player=='w':
            comp_win+=1
        elif player=='g':
            user_win+=1
    
    elif computer=='w':
        if player=='s':
            user_win+=1
        elif player=='g':
            comp_win+=1

    elif computer=='g':
        if player=='w':
            user_win+=1
        elif player=='s':
            comp_win+=1

    if user_win>comp_win:
        print(f"You won round {rounds}")
    elif user_win<comp_win:
        print(f"Computer won round {rounds}")
    else:
        print("Draw\n")

    rounds+=1

if user_win>comp_win:
    print("Congratulations, You won!")
elif user_win<comp_win:
    print("You lose!")
else:
    print("Match Draw\n")



