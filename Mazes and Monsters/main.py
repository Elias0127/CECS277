# Elias Woldie
# Design Pattern --> Singleton
# This program allows the user to wander through a dungeon maze and fight monsters that they encounter as they explore.

import map
import check_input
import hero
import enemy
import random


"""
    Asking the name for our hero. And creating the boolean function "if not false" to start the while loop and start the game.
  """


def main():
    username = input("Enter the your name, traveler: ")
    user = hero.Hero(username)
    game_map = map.Map()
    exit = 0

    while exit != 1:
        """
        Checking the boundaries and making sure that the hero only moves in between the specified limit of the grid. 
        And also checking the boolean validity of the other values such as m, h, etc to decide what happens once they are landed upon by the hero
      """
        if user.hp == 0:
            exit = 1

        print(user)
        print(game_map.show_map(user._loc))
        choice = check_input.get_int_range("""
1. Go North 
2. Go South 
3. Go East 
4. Go West
5. Quit
  Enter choice: 
    """, 1, 5)

        game_map.reveal(user._loc)
        if choice == 1:
            border_check = user.go_north()
        elif choice == 2:
            border_check = user.go_south()
        elif choice == 3:
            border_check = user.go_east()
        elif choice == 4:
            border_check = user.go_west()
        elif choice == 5:
            exit = 1

        if game_map[user._loc[0]][user._loc[1]] == "m":
            monster = enemy.Enemy()
            option = ""
            while option != 2 and monster.hp != 0:
                option = check_input.get_int_range(f"""
  1. Attack {monster}
  2. Run Away
    Enter choice:
        """, 1, 2)
                if option == 1:
                    print(user.attack(monster))
                    if monster._hp != 0:
                        print(monster.attack(user))
                    else:
                        print(f"You have slain a {monster}")
                        game_map.remove_at_loc(user._loc)
            if option == 2:
                random_direction = random.randint(1, 4)
                if random_direction == 1:
                    user.go_north()
                elif random_direction == 2:
                    user.go_south()
                elif random_direction == 3:
                    user.go_east()
                elif random_direction == 4:
                    user.go_west()

        if border_check == "x":
            print("You cannot go that way...")

        if game_map[user._loc[0]][user._loc[1]] == "n":
            print("There is nothing here...")

        if game_map[user._loc[0]][user._loc[1]] == "s":
            print("You are somehow back at the start")

        if game_map[user._loc[0]][user._loc[1]] == "i":
            print("You found a Health Potion! you drink it to restore your health")
            user.heal()

        if game_map[user._loc[0]][user._loc[1]] == "f":
            print("""
Congratulations! You found the exit! 

GAME OVER
      """)
            exit = 1


main()
