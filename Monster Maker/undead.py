from monster import Monster

class Undead(Monster):
    """ Undead class initializes the default name and hp of an Undead monster. Contains an
    attack method for an Undead monsters base attack. """
    def __init__(self):
        """ Initializes the Undead's name and hp by calling super(Monster) which contains
        the getter and setter properties of a Monster. """
        super().__init__("Undead", 6)

    def attack(self):
        """ Attack method returns an integer value representing an attack value. """
        self._base_attack = 6
        return self._base_attack