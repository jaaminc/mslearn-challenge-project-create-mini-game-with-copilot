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

# Write a python function that show options and ask for an option and return it in lower case
def ask_option():
    print("Options (", options + ") :")
    option = input("Enter your option : ")
    option = option.lower()
    return option

# Write a python function that check who is the winner
def winner(option1, option2):
    if option1 == option2:
        return "Tie"
    elif (option1 == "rock" and option2 == "scissors") or (option1 == "scissors" and option2 == "paper") or (option1 == "paper" and option2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# Write a python function that check if the game is over and check the input in lower case is yes o no
def game_over():
    while True:
        game_over = input("Do you want to play again? (yes/no): ")
        game_over = game_over.lower()
        if game_over == "yes":
            return "yes"
        elif game_over == "no":
            return "no"
        else:
            print("Invalid option")


# Write a python function that play the game
def play_game():
 
    player1_wins = 0    
    player1_ties = 0
    rounds = 0

    while True:
        option1 = ask_option()
        if check_option(option1, options):
            option2 = random_option(options)
            print("Player 2: " + option2)
            print(winner(option1, option2))
            rounds += 1
            if winner(option1, option2) == "Player 1 wins":
                player1_wins += 1
            elif winner(option1, option2) == "Tie":
                player1_ties += 1
            if game_over() == "no":
                break
        else:
            print("Invalid option")

    print("Player 1 wins:", player1_wins)
    print("Player 1 ties:", player1_ties)
    print("Player 1 losses:", rounds - player1_wins - player1_ties)
    print("Total rounds:", rounds)
play_game()