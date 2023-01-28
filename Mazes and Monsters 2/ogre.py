from entity import Entity
import random

class Ogre(Entity):
    """ Ogre defines the characteristics of a ogre at the expert level. """

    def __init__(self):
        """ Initiliazes random hp 8-12 and the name of the ogre. """
        random_hp = random.randint(8,12)
        super().__init__("Horrible Ogre", random_hp)

    def attack(self, entity):
        """ Sets an attack level for the ogre 6-10 and attacks the entity.
        Passes in the entity(hero) being attacked.
        Returns a string describing the event.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        self._random_damage = random.randint(6,10)
        entity.take_damage(self._random_damage)
        return "Horrible Ogre attacks " + entity.name + " for " + str(self._random_damage) + " damage."
