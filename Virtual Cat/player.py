
class Player:
    """ Represents the player of the game with life points (hp) initially set to
    25. Can take damage, and has a __str__ method for returning their hp. """
    def __init__(self):
        """ Initializes life points (hp) to 25 """
        self._hp = 25

    @property
    def hp(self):
        """ Returns life points """
        return self._hp

    def take_damage(self, dmg):
        """ Takes damage on the players hp. Passes in the damage value (dmg) and
        subtracts it from hp. If the players life points go below 0 reset to 0. """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """ String representation of the players life points """
        return "\nYour HP: " + str(self._hp)