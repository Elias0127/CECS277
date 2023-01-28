from entity import Entity
import random

class Goblin(Entity):
    """ Easy Golbin defines the characteristics of a goblin at the expert level. """
    def __init__(self):
        """ Initiliazes random hp 6-10 and the name of the goblin. """
        random_hp = random.randint(6,10)
        super().__init__("Bad Goblin", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the goblin 4-8 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(4,8)
        entity.take_damage(self._random_damage)
        return "Bad Goblin attacks " + entity.name + " for " + str(self._random_damage) + " damage."
