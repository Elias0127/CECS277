from entity import Entity
import random

class Troll(Entity):
    """ Troll defines the characteristics of a troll at the expert level. """
    def __init__(self):
        """ Initiliazes random hp 10-14 and the name of the troll. """
        random_hp = random.randint(10,14)
        super().__init__("Angry Troll", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the troll 8-12 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(8,12)
        entity.take_damage(self._random_damage)
        return "Angry Troll attacks " + entity.name + " for " + str(self._random_damage) + " damage."
