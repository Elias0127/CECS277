# Elias Woldie
# Python –-> Functions
# This program allows a user to play Rock-Paper-Scissors against the computer.

import random
import check_input


def weapon_menu():
    """This function is for the user to input their choice: (R)ock, (P)aper, (S)cissors,
    or to go (B)ack. And it checks for the input's validity and returns the inputted value.


    Returns: user_choice
    Raises:
        Error: throws error if the input doesn't exist in the menu
    """

    # Asking the user to choose weapon
    user_choice = input(
        "Choose your weapon:\n R. Rock\n P. Paper\n S. Scissors\n B. Back\n").capitalize()
    # while loop to check the validity of the input
    while True:
        if user_choice == 'R' or user_choice == 'P' or user_choice == 'S' or user_choice == 'B':
            break
        else:
            print("Invalid input! Please try again")
            user_choice = input(
                "Choose your weapon:\n R. Rock\n P. Paper\n S. Scissors\n B. Back\n").capitalize()
    return user_choice


def comp_weapon():
    """This function is for the computer to randomly choose a weapon from “R”, “P”, or “S”.

    Returns: computer_choice which is the computer's randomly generated choice
    """
    possible_choices = ["R", "P", "S"]
    computer_choice = random.choice(possible_choices)
    return computer_choice


def find_winner(player, comp):
    """This function passes in the two weapons (R, P, or S),
    displays the throws, compares the two weapons and displays the result and returns
    who is the winner of that round (0=Tie, 1=Player, 2=Computer).

    Args: player(char): takes the return value of weapon_menu(), which is the user's choice
    Args: comp(char): takes the return value of comp_weapon(), which is the computer's randomly generated choice

    Return: the winner of that round (0=Tie, 1=Player, 2=Computer).
    """

    if player == comp:
        print(f"You chose {player} \nComputer chose {comp}\nTie")
    elif player == "R":
        if comp == "S":
            print("You chose Rock\nComputer chose Scissors\nYou Win!")
            return 1
        else:
            print("You chose Rock\nComputer chose Paper\nYou Lose!")
            return 2
    elif player == "P":
        if comp == "R":
            print("You chose Paper\nComputer chose Rock\nYou win!")
            return 1
        else:
            print("You chose Paper\nComputer chose Scissors\nYou Lose!")
            return 2
    elif player == "S":
        if comp == "P":
            print("You chose Scissors\nComputer chose Paper\nYou win!")
            return 1
        else:
            print("You chose Scissors\nComputer chose Rock\nYou Lose!")
            return 2


def display_scores(player, comp):
    """This function displays the scores, who is leading and who is loosing, that is calculated in the
    find_winner() function."""

    print("Player = ", player, "\nComputer = ", comp)


def main():
    """This function has a loop that repeats repeatedly asks the user for action, 1 to play the game, 2 to see the score,
    and 3 to quit which will stop the loop

    Raises:
        Error: if the user enters invalid input, outside the menus range 1-3, it throws error and ask them to choose again
    """
    user_action = 0
    player_score = 0
    computer_score = 0
    # This while loop is to repeat asking the user what they want to do until they enter 3 which is to quit.
    while user_action != 3:
        print("RPS Menu:")
        user_action = check_input.get_int_range(
            " 1. Play game\n 2. Show Score\n 3. Quit\n", 1, 3)
        # The if statements here is point the user to their specific choice. If they enter 1, it allows them to play the
        # game by choosing a weapon, if they enter 2, it shows them the score and if they enter 3, they quit the game
        if user_action == 1:
            while True:
                user_weapon = weapon_menu()
                if user_weapon != "B":
                    winner_result = find_winner(user_weapon, comp_weapon())
                    if winner_result == 1:
                        player_score += 1
                    elif winner_result == 2:
                        computer_score += 1
                else:
                    break
        elif user_action == 2:
            display_scores(player_score, computer_score)
        else:
            user_action = 3
            print("Final Score: ")
            display_scores(player_score, computer_score)


main()
