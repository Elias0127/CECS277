# Elias Woldie
# Object-Oriented programming –-> Polymorphism 
# This program creates a game where the user must defeat three dragons to pass the trails.


import hero
import dragon
import fire_dragon
import flying_dragon
import random
import check_input

def main():
    """
    Asks the player's choice of attacking weapons and randomly sets the dragon's weapon of choice to attack back
    """
    username = check_input.get_str("What is your name, challenger? ")
    player = hero.Hero(username, 50)
    print("Welcome to dragon training " + username + "\nYou must defeat 3 dragons. \n")
    # A list of dragon types for the player to attack
    dragons = [dragon.Dragon("Deadly Nadder", 10),
               fire_dragon.FireDragon("Gronckle", 15, 3),
               flying_dragon.FlyingDragon("Timberjack", 20, 5)]
    # Checks if any dragons left to attack
    while len(dragons) > 0:
        # Asks the player which dragons to attack
        dragon_attack = check_input.get_int_range(("1. Attack" + str(dragons[0]) + ": \n2. Attack" + str(dragons[1]) + ": \n3. Attack" + str(dragons[2]) + "\nChoose a dragon to attack: "), 1, 3)
        dragon_attack -= 1
        # Asks the player which weapon they want to use
        attack_weapon = check_input.get_int_range("\n1. Arrow (1 D12) \n2. Sword (2 D6) \nEnter weapon: ", 1, 2)
        if attack_weapon == 1:
            print(player.arrow_attack(dragons[dragon_attack]))
        if attack_weapon == 2:
            print(player.sword_attack(dragons[dragon_attack]))
        #  If the user defeats the dragon (hp is 0), then remove that dragon from the list.
        if dragons[dragon_attack].hp <= 0:
            del dragons[dragon_attack]
        # Chooses a random (surviving) dragon that will attack the user
        surviving_dragon = random.choice(dragons)
        # Chooses a random (attacking) method the dragon will use
        random_attack = random.randint(1, 3)
        if random_attack == 1:
            print(surviving_dragon.basic_attack(player))
        else:
            print(surviving_dragon.special_attack(player))
        if player.hp == 0:
            print("End")
            break
        if len(dragons) < 3:
            print("Congratulations! You have defeated all 3 dragons, you have passed the trials. ")
            break

main()