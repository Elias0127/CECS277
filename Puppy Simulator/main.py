# Elias Woldie
# Design Pattern --> State
# This program creates a puppy simulator program that has two basic functions: to feed or play with the puppy.  The puppy will react differently to these functions based on which state it is currently in.  The puppy has three possible states: asleep, eating, or playing.

import check_input
import puppy

def main():
    """ Main: represents a puppy that can eat, play, and sleep """
    print("Puppy Simulator")
    print("Congratulations on you new puppy!")
    pup = puppy.Puppy() # creates a puppy
    # while loop for asking the user if they'd like to feed or play with the puppy
    interaction = 0
    while interaction != 3:
        # gets input from user
        interaction = check_input.get_int_range("What would you like to do?\n1. Feed the puppy"
                                                "\n2. Play with the puppy\n3. Quit\nEnter choice: (1,2,3)", 1, 3)
        # if the user would like to feed the puppy
        if interaction == 1:
            print(pup.give_food()) # feeds the puppy
            print(pup.feeds)
        # if the user would like to play with the puppy
        elif interaction == 2:
            print(pup.throw_ball()) # plays with the puppy
            print(pup.plays)

main()