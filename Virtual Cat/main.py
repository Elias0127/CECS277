# Elias Woldie
# Object-Oriented programming –-> Abstract Class
# This program creates an interactive pet game where the user has life points and interacts with different types of cats.

from tabby import Tabby
from ocelot import Ocelot
from tiger import Tiger
from player import Player
import check_input


def interact_cat(cat, player):
    """ Interact method for interacting with the cat. Takes in a cat and a player. Takes
    an input from the user on whether to feed, play, or pet the cat.
    Attributes:
        cat (Cat): either Tabby, Ocelot, or Tiger type
        player (Player): represents the player
    """
    # users choice of feed, play, or pet
    interaction_input = check_input.get_int_range("Cat Menu:\n1. Feed\n2. Play\n"
                                                  "3. Pet\nEnter choice (1-3)\n", 1, 3)
    # feed the cat
    if interaction_input == 1:
        print(cat.feed(player))
    # play with the cat
    if interaction_input == 2:
        print(cat.play(player))
    # pet the cat
    if interaction_input == 3:
        print(cat.pet(player))


def main():
    """ Main """
    user = Player()
    # gets the type of cat
    cat_selection = check_input.get_int_range("Cat Selection: \n1. Tabby\n"
                                              "2. Ocelot\n3. Tiger\n", 1, 3)
    # create a Tabby cat with a name
    if cat_selection == 1:
        cat_name = input("Enter your cat's name: ")
        c = Tabby(cat_name)
    # create an Ocelot cat with a name
    elif cat_selection == 2:
        cat_name = input("Enter your cat's name: ")
        c = Ocelot(cat_name)
    # create a Tiger with a name
    elif cat_selection == 3:
        cat_name = input("Enter your cat's name: ")
        c = Tiger(cat_name)
    # while the user still has hp continue playing the game
    while user._hp != 0:
        interact_cat(c, user)  # calling interact_cat function
        print(user)
        print(c)
    # if the user has 0 hp end game
    if user._hp == 0:
        print("You died")


main()
