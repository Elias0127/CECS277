
from cat import Cat
import random

class Tabby(Cat):
    """ Represents a Tabby cat. Has a name and hunger level from the Cat class.
    Is able to get fed, pet, and play. Depending on which activity the cats hunger
    level changes and the cat may attack the player. """
    def feed(self, player):
        """ Represents the act of the Tabby cat getting fed. Depending on the Tabby
        cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        # if the cats hunger level is >= 7 update its hunger accordingly
        if self._hunger >= 7:
            self.update_hunger(random.randint(0,1)) # updates hunger by either 0 or 1
            return "I'm not hungry, thank you."
        # if the cats hunger level is between 3 and 7 update its hunger and take hp from player accordingly
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(1,3)) # updates hunger between 0 and 3 integers
            player.take_damage(random.randint(0,3)) # removes hit points from player between 0 and 3 points
            return "I'm not hungry, but I'm not full"
        # if the cat is very hungry update its hunger and attack player
        elif self._hunger <= 3:
            self.update_hunger(random.randint(1,5)) # updates hunger between 0 and 5
            player.take_damage(random.randint(1,5)) # takes hit points from player between 0 and 5
            return "I'm hungry, I want food, watch out I bite."

    def play(self, player):
        """ Represents the act of the Tabby cat getting played with. Depending on the
        Tabby cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-1,0)) # removes 0 or 1 from cats hunger level
            return "Too full to play"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-5,-1)) # removes between 0 and -5 from cats hunger
            player.take_damage(random.randint(1,3)) # removes between 0 and 3 hit points from player
            return "I love to play"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-3,0)) # removes between -3 and 0 from cats hunger
            player.take_damage(random.randint(1,5)) # removes between 0 and 5 hp from player
            return "I'm hungry, watch out I bite"

    def pet(self, player):
        """ Represents the act of the Tabby cat getting pet. Depending on the Tabby
        cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat.
        Attributes:
            player (Player): represents the player
        """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-1,0)) # removes 0 or 1 from cats hunger level
            return "I love to be pet"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-3,0)) # removes between 0 and -3 from cats hunger
            player.take_damage(random.randint(1,3)) # removes between 0 and 3 hit points from player
            return "I was a little hungry I'm sorry if I bit you"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-3,0)) # removes between -3 and 0 from cats hunger
            player.take_damage(random.randint(1,5)) # removes between 0 and 5 hp from player
            return "Watch out, I bite when I'm really hungry"


