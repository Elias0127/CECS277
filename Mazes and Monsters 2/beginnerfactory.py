
from enemyfactory import EnemyFactory
from easytroll import EasyTroll
from easyogre import EasyOgre
from easygoblin import EasyGoblin
import random

class BeginnerFactory(EnemyFactory):
    """ Beginner Factory inherits from EnemyFactory Interface. """
    def create_random_enemy(self):
        """ Creates random enemies. """
        randomEnemy = random.randint(1,3)
        if randomEnemy == 1:
            randomEnemy = EasyTroll() # creates Easy Troll
        elif randomEnemy == 2:
            randomEnemy = EasyOgre() # creates Easy Ogre
        elif randomEnemy == 3:
            randomEnemy = EasyGoblin() # creates Easy Goblin
        return randomEnemy