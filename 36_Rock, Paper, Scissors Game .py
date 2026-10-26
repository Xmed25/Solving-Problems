# Rock, Paper, Scissors Game 

# Write a program to simulate a game of Rock, Paper, Scissors.  
# The game will prompt the player to choose rock, paper, or scissors by typing 'r', 
# 'p', or 's'. The computer will randomly select its choice. The game will then display 
# both choices using emojis and determine the winner based on the rules. 

# Optional Enhancements 

# • Modify the game so that the first player (or computer) to win two out of three 
# rounds is declared the overall winner. This adds a competitive aspect to the 
# game. 

# • Keep a tally of how many times the player wins, loses, or ties with the 
# computer. Display these statistics at the end of the game. 

# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs.


import random as rn

def game():
    choices = ['r', 'p', 's']
    computer_result = 0
    player_result = 0

    while computer_result < 3 and player_result < 3:
        choice = input("Rock, Paper, or Scissors? (r/p/s): ")
        choice = choice.lower().strip()

        if choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = rn.choice(choices)

        print(f"Your choice: {choice}")
        print(f"Computer choice: {computer_choice}")

        if choice == computer_choice:
            print("DRAW!")

        elif (
            (choice == 'r' and computer_choice == 's')
            or (choice == 'p' and computer_choice == 'r')
            or (choice == 's' and computer_choice == 'p')
        ):
            player_result += 1
            print("You win this round!")

        else:
            computer_result += 1
            print("Computer wins this round!")

        print(f"Score: You {player_result} - {computer_result} Computer")
        print("-" * 30)

    if player_result == 3:
        print("Congratulations! You won the game!")
    else:
        print("Game over! Computer won!")

game()
