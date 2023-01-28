import dragon
import random


class FireDragon(dragon.Dragon):
    """
    Attributes: _fire_shots(int): the number of fire shots
    """
    def __init__(self, name, max_hp, f_shots):
        """Initializes the name and hp, then set the number of fire_shots. """
        super().__init__(name, max_hp)
        self._fire_shots = f_shots

    def special_attack(self, hero):
        """Overrides fire attack"""
        # if the dragon has any fire_shots left, then the hero takes a random amount of damage
        if self._fire_shots > 0:
            fire_attack = random.randrange(5, 9)
            self._fire_shots -= 1
            hero.take_damage(fire_attack)
            return "\n" + self._name + " shot fire attack! " + "for " + str(fire_attack) + " damage!"
        else:
            return "\n" + self._name + " failed a fire attack "

    def __str__(self):
        """Returns the number of fire shots remaining in a string format"""
        return super().__str__() + " \nFire Shots Remaining : " + str(self._fire_shots)
