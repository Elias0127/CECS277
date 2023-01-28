
from monster import Monster

class Beast(Monster):
    """ Beast class initializes the default name and hp of an Beast monster. Contains an
        attack method for a Beast monsters base attack. """
    def __init__(self):
        """ Initializes the Beast's name and hp by calling super(Monster) which contains
        the getter and setter properties of a Monster. """
        super().__init__("Beast", 4)

    def attack(self):
        """ Attack method returns an integer value representing an attack value. """
        self._base_attack = 4
        return self._base_attack