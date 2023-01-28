
import abc

class Cat(abc.ABC):
    """ Represents a Cat with a name and hunger level. The cats hunger can be updated
    depending on their activity and if they are being fed. The cat is able to get fed,
    play, and be pet.
    Attributes:
        name (str) = name of cat
    """

    def __init__(self, name):
        """ Initializes the name of the cat.
        Attributes:
            name (str): name of cat
        """
        self._name = name
        self._hunger = 5 # initializes hunger of cat to 5

    @property
    def name(self):
        """ Returns the cats name """
        return self._name

    @property
    def hunger(self):
        """ Returns the cats hunger level """
        return self._hunger

    def update_hunger(self, val):
        """ Updates the cats hunger. Gets passed a value (val) to adjust the cats
        hunger level with. If the cats hunger level is less than 0, resets it to 1.
        If it's greater than 10, then resets it to 10.
        Attributes:
            val (int): value to either increase or decrease the cat's hunger
        """
        self._hunger += val
        # if hunger is equal to 0 or goes below 0 reset it to 1
        if self._hunger <= 0:
            self._hunger = 1
        # if hunger is greater than 10 reset it to 10
        elif self._hunger > 10:
            self._hunger = 10

    @abc.abstractmethod
    def feed(self, player):
        """ Abstract feed method stub. Gets passed a player to feed the cat. """
        pass # does nothing

    @abc.abstractmethod
    def play(self, player):
        """ Abstract play method stub. Gets passed a player to play with the cat. """
        pass

    @abc.abstractmethod
    def pet(self, player):
        """ Abstract pet method stub. Gets passed a player to pet the cat. """
        pass

    def __str__(self):
        """ Returns a string representation of the cat."""
        # for loop concatenating a string for the hunger level of the cat
        # returns the cats name and hunger level
        h = ""
        for i in range(self._hunger):
            h += " + "
        return "Cat: " + self._name + "\nHunger Level: \nStarving                    Full\n" \
                                       "|" + h + "|"
