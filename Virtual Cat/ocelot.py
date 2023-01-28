
from cat import Cat
import random

class Ocelot(Cat):
    """ Represents an Ocelot cat. Has a name and hunger level from the Cat class.
        Is able to get fed, pet, and play. Depending on which activity the cats hunger
        level changes and the cat may attack the player. """
    def feed(self, player):
        """ Represents the act of the Ocelot cat getting fed. Depending on the Ocelot
        cats hunger level, the hunger level changes and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        if self._hunger >= 7:
            self.update_hunger(random.randint(0,1))
            return "I'm not hungry, thank you"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(1,3))
            player.take_damage(random.randint(0,3))
            return "I'm not hungry, but I'm not full"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(1,5))
            player.take_damage(random.randint(1,5))
            return "I'm hungry, I want food, watch out I bite."

    def play(self, player):
        """ Represents the act of the Ocelot cat getting played with. Depending on the
        Ocelot cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-1,0))
            return "Too full to play"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-5,-1))
            player.take_damage(random.randint(1,3))
            return "I love to play"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-3,0))
            player.take_damage(random.randint(1,5))
            return "I'm hungry, watch out I bite"

    def pet(self, player):
        """ Represents the act of the Ocelot cat getting pet. Depending on the
        Ocelot cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-1,0))
            return "I love to be pet"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-3,0))
            player.take_damage(random.randint(1,3))
            return "I was a little hungry I'm sorry if I bit you"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-3,0))
            player.take_damage(random.randint(1,5))
            return "Watch out, I bite when I'm really hungry"

