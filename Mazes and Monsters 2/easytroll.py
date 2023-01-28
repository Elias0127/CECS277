
from entity import Entity
import random

class EasyTroll(Entity):
    """ Easy Troll defines the characteristics of a troll at the beginner level. """
    def __init__(self):
        """ Initiliazes random hp 4-5 and the name of the troll. """
        random_hp = random.randint(4,5)
        super().__init__("Easy Troll", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the troll 1-5 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(1, 5)
        entity.take_damage(self._random_damage)
        return "Easy Troll attacks " + entity.name + " for " + str(self._random_damage) + " damage."

