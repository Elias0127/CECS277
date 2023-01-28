from entity import Entity
import random
from map import Map

class Hero(Entity):
    """
    Hero class represents the user with a name, hp, and location. Inherits from the Entity
    class.
    """

    @property
    def loc(self):
        """ Returns the location of the hero. """
        return self._loc

    def __init__(self, name):
        """ Initializes the hero with a name and hp by calling super(). """
        super().__init__(name, 25)
        self._loc = [0,0] # sets the initial location of the hero

    def attack(self, entity):
        """ Heroes attack method contains a random attack damage value between 2-5
        to attack the enemy. Returns a description of the attack.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(2,5)
        entity.take_damage(self._random_damage)
        return self._name + " attacks " + entity.name + " for " + str(self._random_damage) + " damage."

    def go_north(self):
        """ Method for moving the hero north on the map. Returns "x" if the location is
        off the map, otherwise returns the location of the hero on the map. """
        if self._loc[0] == 0:
            return "x"
        else:
            self._loc[0] = self._loc[0] - 1 # moves the location of the hero north by 1 position
            _map = Map() # constructs the map
            return _map[self._loc[0]][self._loc[1]]

    def go_south(self):
        """ Method for moving the hero south on the map. Returns "x" if the location is
        off the map, otherwise returns the location of the hero on the map. """
        _map = Map() # constructs the map
        if self._loc[0] == len(_map) - 1:
            return "x"
        else:
            self._loc[0] = self._loc[0] + 1 # moves the hero south 1 position
            return _map[self._loc[0]][self._loc[1]]

    def go_east(self):
        """ Method for moving the hero east on the map. Returns "x" if the location is
        off the map, otherwise returns the location of the hero on the map. """
        _map = Map() # constructs the map
        if self._loc[1] == len(_map) - 1:
            return "x"
        else:
            self._loc[1] = self._loc[1] + 1 # moves the hero east 1 position
            return _map[self._loc[0]][self._loc[1]]

    def go_west(self):
        """ Method for moving the hero west on the map. Returns "x" if the location is
        off the map, otherwise returns the location of the hero on the map. """
        if self._loc[1] == 0:
            return "x"
        else:
            self._loc[1] = self._loc[1] - 1 # moves the hero west 1 position
            _map = Map() # constructs the map
            return _map[self._loc[0]][self._loc[1]]
