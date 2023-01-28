# Elias Woldie
# Design Pattern --> Decorator Pattern 
# This program creates a monster make program that uses three base types of monsters(ie. Alien, Beast, Undead).Those monsters can then be decorated with four different monster abilities(ie. Fire, Lasers, Flying, Poison).  The program will then display the updated stats for the constructed monster.

import check_input
from alien import Alien
from beast import Beast
from undead import Undead
from fire import Fire
from flying import Flying
from lasers import Lasers
from poison import Poison

def main():
    """ Main : presents a menu to the user and prompts them what type of monster they would
    like to create. Then continues to prompt them what abilities they would like to attach
    to the monster until the user chooses to quit. """

    print("Monster Maker!")
    # if statements creating a specific monster based on users input
    monster = check_input.get_int_range("Choose a base monster (Enter 1, 2, or 3): ", 1, 3)
    if monster == 1:
        monster = Alien() # creates monster of Alien type
        print(monster)
    elif monster == 2:
        monster = Beast()
        print(monster)
    elif monster == 3:
        monster = Undead()
        print(monster)

    # Loop prompting user what abilities they'd like to give the monster
    ability = None
    while(ability != 5):
        ability = check_input.get_int_range("Add an ability (Enter 1, 2, 3, 4, or 5):"
                                            "\n1. Fire\n2. Flying\n3. Lasers\n4. Poison"
                                            "\n5. Quit\n", 1, 5)

        if ability == 1:
            monster = Fire(monster) # adds Fire ability to monster
            print(monster)
        if ability == 2:
            monster = Flying(monster) # adds Flying ability to monster
            print(monster)
        if ability == 3:
            monster = Lasers(monster) # adds Laser ability to monster
            print(monster)
        if ability == 4:
            monster = Poison(monster) # adds Poison ability to monster
            print(monster)

main()