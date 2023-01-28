from entity import Entity
import random

class EasyOgre(Entity):
    """ Easy Ogre defines the characteristics of a ogre at the beginner level. """
    def __init__(self):
        """ Initiliazes random hp 3-5 and the name of the ogre. """
        random_hp = random.randint(3,5)
        super().__init__("Easy Ogre", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the ogre 1-4 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(1, 4)
        entity.take_damage(self._random_damage)
        return "Easy Ogre attacks " + entity.name + " for " + str(self._random_damage) + " damage."
