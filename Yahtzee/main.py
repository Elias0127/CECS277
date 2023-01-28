# Elias Woldie
# Object-Oriented programming –-> Class Relationships
# This program creates a dice game that awards the user points for pair, three-of-a-kind, or a series.

import check_input
import player


def take_turn(player):
    """
    Roll the player’s dice, display the dice, check for and display any win types (pair, series, three-of-a-kind), and
    display the updated score.
    """
    player.roll_dice()
    print(player)
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_pair():
        print("You got a pair!")
    elif player.has_series():
        print("You got a series of 3")
    else:
        print("Aww. Too Bad.")
    print("Score = ", player.get_points())


def main():
    """
    Construct a player object, and then repeatedly call take_turn until the user chooses to end the game.
    """
    dice = player.Player()
    choice = True
    # Asking the user repeatedly if they want to play again
    while choice:
        choice = check_input.get_yes_no("Play Again? (Y/N): \n")
        if choice:
            take_turn(dice)
        elif not choice:
            break
    print("Game Over\n Final Score = ", dice.get_points())


main()
