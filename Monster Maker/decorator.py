from monster import Monster
import abc

class Decorator(Monster,abc.ABC):
    """ Decorator class inherits from the Monster class and calls super to initialize
    the monster that is passed into the Decorator class. Also creates an instance of
    the monster for the monsters attack method. """
    def __init__(self, monst):
        """ Initializes the monsters name and hp by calling its super class(Monster),
        and creates an instance of the monster.
        Attributes:
             monst (Monster): represents a monster
        """
        super().__init__(monst.name, monst.hp)
        self._monster = monst

    def attack(self):
        """ Returns the monsters attack method. """
        return self._monster.attack()
