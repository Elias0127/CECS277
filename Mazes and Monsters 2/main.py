# Elias Woldie
# Design Pattern --> Factory Method
# This program allows a user to navigate around a map encountering monsters

from hero import Hero
from map import Map
import check_input
import random
from beginnerfactory import BeginnerFactory
from expertfactory import ExpertFactory


def main():
    """ Main contains a hero on a map who encounters different monsters of specified
    difficulty level. Game continues until either the hero dies or the user ends the game.
    """

    user_name = input("What is your name, traveler? ")
    # difficulty input
    difficulty_level = check_input.get_int_range("Difficulty:\n1. Beginner\n"
                                                 "2. Expert\nEnter 1 or 2: ", 1, 2)

    hero = Hero(user_name)  # constructs a hero
    m_map = Map()  # constructs the map for the game
    m_map.reveal(hero.loc)  # reveals the location of the hero on the map

    # if statements constructing either a beginner factory or expert factory based on input
    if difficulty_level == 1:
        factory = BeginnerFactory()
    elif difficulty_level == 2:
        factory = ExpertFactory()

    map_counter = 1  # counter for changing the from map1, map2, and map3

    # while loop continuing until hero either dies or ends the game
    valid = False
    while not valid:

        # if the hero dies end the game
        if hero.hp == 0:
            break

        print(hero.__str__())  # prints the hero name and hp level
        print(m_map.show_map(hero.loc))  # prints the map with the hero on it
        # gets user input for the direction they want to go
        user_direction = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East"
                                                   "\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)

        # if statements moving the hero on the map and revealing the location of the hero
        # each direction contains an if statement checking if hero lands on a "x" which
        # signifies the user cannot go in that direction
        if user_direction == 1:
            north = hero.go_north()
            m_map.reveal(hero.loc)
            if north == "x":
                print(hero.name + ", you cannot go that way.")
        elif user_direction == 2:
            south = hero.go_south()
            m_map.reveal(hero.loc)
            if south == "x":
                print(hero.name + ", you cannot go that way.")
        elif user_direction == 3:
            east = hero.go_east()
            m_map.reveal(hero.loc)
            if east == "x":
                print(hero.name + ", you cannot go that way.")
        elif user_direction == 4:
            west = hero.go_west()
            m_map.reveal(hero.loc)
            if west == "x":
                print(hero.name + ", you cannot go that way.")
        elif user_direction == 5:
            break

        # if the heroes location == "n" on the map signifies room is empty
        if m_map[hero.loc[0]][hero.loc[1]] == "n":
            print(hero.name + ", the room your in is empty.")
        # if the heroes location == "x" on the map, cannot go that way
        elif m_map[hero.loc[0]][hero.loc[1]] == "x":
            print(hero.name + ", you cannot go that way.")
        # if the heroes location == "s" on the map signifies hero is back at the start
        elif m_map[hero.loc[0]][hero.loc[1]] == "s":
            print(hero.name + ", your back at the start.")
        # if the heroes location == "i" on the map signifies the hero found a health potion
        elif m_map[hero.loc[0]][hero.loc[1]] == "i":
            print(hero.name + ", you found a health potion")
            hero.heal()
            m_map.remove_at_loc(hero.loc)
        # if the heroes location == "m" on the map signifies hero found a monster
        elif m_map[hero.loc[0]][hero.loc[1]] == "m":
            # constructs a monster from the beginner/expert factory
            enemy = factory.create_random_enemy()
            print(hero.name + " encounters a " + str(enemy))
            # while loop for users decision to either attack or run
            monster_presence = True
            while monster_presence == True:
                attack_run_input = check_input.get_int_range("1. Attack " + enemy.name
                                                             + "\n2. Run away\nEnter choice: ", 1, 2)
                # if user decides to attack the monster
                if attack_run_input == 1:
                    print(hero.attack(enemy))  # attacks monster
                    # attacks hero if monster is still alive
                    if enemy.hp > 0:
                        print(enemy.attack(hero))
                    # if hero dies, exits loop
                    elif hero.hp == 0:
                        print(enemy.name + " has killed " + hero.name)
                        monster_presence = False
                    # if hero kills the monster exits loop
                    else:
                        print(hero.name + " has killed the " + enemy.name)
                        # also removes monster from map
                        m_map.remove_at_loc(hero.loc)
                        monster_presence = False
                # if user decides to run from monster, picks a random direction for hero, and exits loop
                elif attack_run_input == 2:
                    print(hero.name + " has decided to run away.")
                    user_direction = random.randint(1, 4)
                    if user_direction == 1:
                        hero.go_north()
                        m_map.reveal(hero.loc)
                    if user_direction == 2:
                        hero.go_south()
                        m_map.reveal(hero.loc)
                    if user_direction == 3:
                        hero.go_east()
                        m_map.reveal(hero.loc)
                    if user_direction == 4:
                        hero.go_west()
                        m_map.reveal(hero.loc)
                    monster_presence = False

        # if heroes location == "f", the hero has found the entrance to the next map
        elif m_map[hero.loc[0]][hero.loc[1]] == "f":
            print(hero.name + ", you have found the entrance to the next map.")

            # increments map_counter for changing maps
            map_counter += 1
            if map_counter > 3:
                map_counter = 1
            m_map.load_map(map_counter)  # loads the next map


main()
