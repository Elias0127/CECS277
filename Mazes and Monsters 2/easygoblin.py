from entity import Entity
import random

class EasyGoblin(Entity):
    """ Easy Goblin defines the characteristics of a goblin at the beginner level. """
    def __init__(self):
        """ Initiliazes random hp 3-4 and the name of the goblin. """
        random_hp = random.randint(3,4)
        super().__init__("Easy Goblin", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the goblin 1-3 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(1, 3)
        entity.take_damage(self._random_damage)
        return "Easy Goblin attacks " + entity.name + " for " + str(self._random_damage) + " damage."
