import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            return("Rock smashes scissors! You win!")
        else:
            return("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            return("Paper covers rock! You win!")
        else:
            return("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            return("Scissors cuts paper! You win!")
        else:
            return("Rock smashes scissors! You lose.")
round = 0
win = 0
computer_win = 0
while True:
    round +=1
    print(f"Round {round}:")
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue
    computer_action = get_computer_selection()
    #determine_winner(user_action, computer_action)
    print(determine_winner(user_action, computer_action))

    if "You win" in determine_winner(user_action, computer_action):
        win +=1
    elif "You los" in determine_winner(user_action, computer_action):
        computer_win += 1
    elif "It's a tie!" in  determine_winner(user_action, computer_action):
        win +=0
        computer_win +=0

    print(f"Player: {win} \nComputer: {computer_win}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break