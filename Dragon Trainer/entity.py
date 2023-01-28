class Entity:
    """
    sets the name of the dragon and hit point
    Attributes:
        _name(str): name of the dragon
        _max_hp(int): maximum hit point
        _hp(int): hit point
    """
    def __init__(self, name, max_hp):
        """Initializes name of the dragon, the maximum hit point the dragon takes"""
        self._name = name
        self. _max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def take_damage(self, dmg):
        """Takes the damage the dragon takes"""
        self._hp = self._hp - dmg
        "Checks if the hp is not negative "
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """
        Display the entity’s name and hp in a string format
        """
        return self._name + ": " + str(self._hp) + "/" + str(self._max_hp)





