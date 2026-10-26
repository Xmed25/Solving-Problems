# Dice Rolling Game  

# Write a program that simulates rolling a pair of dice. Each time the program runs, it 
# should randomly generate two numbers between 1 and 6 (inclusive), representing 
# the result of each die. The program should then display the results and ask if the 
# user would like to roll again. 

# Optional Enhancements 

# • Modify the program so the user can specify how many dice they want to roll. 
# • Add a feature that keeps track of how many times the user has rolled the dice 
# during the session. This will require a counter that increments each time the 
# dice are rolled. 

import random as rn

def game():
    times=0
    while True:
        dice=input("Roll The Dice ?: (y/n): ")
        if dice.strip().lower()=='y':
            times+=1
            random_dice1=rn.randint(1,6)
            random_dice2=rn.randint(1,6)
            dices=(random_dice1,random_dice2)
            print(dices)
        else:
            print(f"Times has rolled : {times}")
            return 0
game()
