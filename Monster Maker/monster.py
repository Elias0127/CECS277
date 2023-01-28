import abc

class Monster(abc.ABC):
    """ Monster class provides the layout for a monster with a name and hp. Has a string
    method that represents the monster and an abstract attack method which forces child
    classes to override it. """
    def __init__(self, name, hp):
        """ Initializes the name and hp of the monster by setting the name and hp passed
        in to its own name and hp property methods.
        Attributes:
            name (str): name of monster
            hp (int): hp of monster
        """
        self.hp = hp
        self.name = name

    @property
    def name(self):
        """ Returns name of monster """
        return self._name

    @name.setter
    def name(self, name):
        """ Sets name of monster """
        self._name = name

    @property
    def hp(self):
        """ Returns hp of monster """
        return self._hp

    @hp.setter
    def hp(self, hp):
        """ Sets hp of monster """
        self._hp = hp

    def __str__(self):
        """ Returns a string representation of the monster. """
        return "Name: " + self.name + "\nHP: " + str(self.hp)\
               + "\nAttack power: " + str(self.attack())

    @abc.abstractmethod
    def attack(self):
        """ Abstract attack method forces inheriting classes to override. """
        pass
