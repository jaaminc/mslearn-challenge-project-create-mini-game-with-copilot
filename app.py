# Write a python program that play rock, scissors, paper game

options = ("rock", "scissors", "paper")

option = ""

# Write a python function that check option is in options
def check_option(option, options):
    if option in options:
        return True
    else:
        return False
    
# Write a python function that return a random option from options
import random
def random_option(options):
    return random.choice(options)

# Write a python function that ask for an option and return it
def ask_option():
    option = input("Enter your option: ")
    return option

# Write a python function that check who is the winner
def winner(option1, option2):
    if option1 == option2:
        return "Tie"
    elif (option1 == "rock" and option2 == "scissors") or (option1 == "scissors" and option2 == "paper") or (option1 == "paper" and option2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# Write a python function that check if the game is over
def game_over():
    return input("Do you want to play again? (yes/no): ")

# Write a python function that play the game
def play_game():
    while True:
        option1 = ask_option()
        if check_option(option1, options):
            option2 = random_option(options)
            print("Player 2: " + option2)
            print(winner(option1, option2))
            if game_over() == "no":
                break
        else:
            print("Invalid option")

play_game()