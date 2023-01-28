import dragon
import random


class FlyingDragon(dragon.Dragon):
    """
    Attributes: _swoops(int): the number of swoops
    """
    def __init__(self, name, max_hp, swoops):
        """Initializes the name and hp, then set the number of swoops. """
        super().__init__(name, max_hp)
        self._swoops = swoops

    def special_attack(self, hero):
        """overrides swoop attack """
        # # if the dragon has any swoops left, then the hero takes a random amount of damage
        if self._swoops > 0:
            swoops_attack = random.randrange(5, 8)
            self._swoops -= 1
            hero.take_damage(swoops_attack)
            return "\n" + self._name + " attacked with swoops attack " + "for " + str(swoops_attack) + " damage!"
        else:
            return self._name + " failed a fire attack\n "

    def __str__(self):
        """Returns the number of swoops remaining in a string format"""
        return super().__str__() + " \nSwoop Shots Remaining : " + str(self._swoops)
