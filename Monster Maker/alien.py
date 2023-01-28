
from monster import Monster

class Alien(Monster):
    """ Alien class initializes the default name and hp of an Alien monster. Contains an
    attack method for an Alien monsters base attack. """
    def __init__(self):
        """ Initializes the Alien's name and hp by calling super(Monster) which contains
         the getter and setter properties of a Monster. """
        super().__init__("Alien", 2)

    def attack(self):
        """ Attack method returns an integer value representing an attack value. """
        self._base_attack = 2
        return self._base_attack