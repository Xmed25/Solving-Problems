# Number Guessing Game 

# Write a program to have the computer randomly select a number between 1 and 
# 100, and then prompt the player to guess the number. The program should give 
# hints if the guess is too high or too low. 


# Optional Enhancements 
# • Allow the user to specify the minimum and maximum values for the number 
# range before the game starts. This gives the player more control over the 
# difficulty level. 

# • Implement a feature that limits the number of guesses a player can make. If 
# the player runs out of attempts, the game should end, and the correct number 
# should be revealed. 

# • Add a feature that keeps track of the fewest attempts it took to guess the 
# number correctly. The program should display this "best score" at the end of 
# each game.


import random as rn

def game():
    attempts=5
    rounds=0
    random_num=rn.randint(1,100)
    while attempts>0:

        try:
            guess=int(input("Guess the Number between(1,100): "))
            print(random_num)

        except ValueError:
            print("Invalid Value ! try again")
            continue

        if guess==random_num:
            print(f"Congratulations ! You Guessed number in {rounds} attempts")

        elif guess<0 or guess==0:
            print("Please Guess the Number between(1,100)")    

        elif guess>random_num:
            attempts-=1
            rounds+=1
            print("Too High ! Try again")

        elif guess<random_num:
            attempts-=1
            rounds+=1
            print("Too Low ! Try again")

    print("You Lose ")
    print("GAME OVER !")
      

game()  
