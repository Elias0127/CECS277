
from enemyfactory import EnemyFactory
from troll import Troll
from ogre import Ogre
from goblin import Goblin
import random

class ExpertFactory(EnemyFactory):
    """ Expert Factory inherits from EnemyFactory Interface. """
    def create_random_enemy(self):
        """ Creates random enemies. """
        randomEnemy = random.randint(1,3)
        if randomEnemy == 1:
            randomEnemy = Troll() # creates Troll
        elif randomEnemy == 2:
            randomEnemy = Ogre() # creates Ogre
        elif randomEnemy == 3:
            randomEnemy = Goblin() # creates Goblin
        return randomEnemy