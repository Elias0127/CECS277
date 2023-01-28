from decorator import Decorator

class Flying(Decorator):
    """ Flying class initializes the monsters name and hp, and passes the modified monster
    to super class. Also, adds to and returns its parent classes attack method. """
    def __init__(self, monst):
        """ Initializes the monster and adds to it's name and hp. Passes the modified
        monster to its super class. """
        monst.name = "Flying " + monst.name
        monst.hp = monst.hp + 4
        super().__init__(monst)

    def attack(self):
        """ Calls the super classes attack method and adds to it. """
        return super().attack() + 4
