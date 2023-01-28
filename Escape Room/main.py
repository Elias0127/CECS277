# Elias Woldie
# Object-Oriented programming –-> Interfaces 
# This program simulates an escape room by having the user open a series of three doors random chosen from several different types of doors.


import random
import basicdoor
import combodoor
import lockeddoor
import check_input


def open_door(door):
    print(door.examine_door())
    choice = check_input.get_int_range(
        door.menu_options(), 1, door.get_menu_max())  # input is within menu
    door.attempt(choice)
    if door.is_unlocked():  # first attempt is good
        print(door.success())
    else:  # incorrect
        while door.is_unlocked() == False:  # runs until door is opened
            print(door.clue())
            choice = check_input.get_int_range(
                door.menu_options(), 1, door.get_menu_max())
            door.attempt(choice)
        print(door.success())


def main():
    print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape.\n")

    doors = [basicdoor.BasicDoor(), lockeddoor.LockedDoor(),
             combodoor.ComboDoor()]

    for i in range(len(doors)):  # runs 3 times
        door_num = random.randint(1, len(doors))
        open_door(doors[door_num - 1])
    print("\nCongratulations! You escaped. . . this time. ")


main()
