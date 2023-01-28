
import abc

class EnemyFactory(abc.ABC):
    """ Abstract Enemy Factory that every Concrete Factory uses. """
    @abc.abstractmethod
    def create_random_enemy(self):
        """ Abstract method that concrete methods use for creating random enemies. """
        pass
