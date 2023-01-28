
from cat import Cat
import random

class Tiger(Cat):

    def feed(self, player):
        """ Represents the act of the Tiger cat getting fed. Depending on the
        Tiger cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat. """
        if self._hunger >= 7:
            self.update_hunger(random.randint(0,3))
            return "I'm not hungry, thank you"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(1,5))
            player.take_damage(random.randint(0,5))
            return "I'm not hungry, but I'm not full"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(1,7))
            player.take_damage(random.randint(1,7))
            return "I'm hungry, I want food, watch out I bite."

    def play(self, player):
        """ Represents the act of the Tiger cat getting played with. Depending on the
        Tiger cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat. """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-3,0))
            return "Too full to play"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-7,-3))
            player.take_damage(random.randint(3,5))
            return "I love to play, I'm sorry if I hurt you"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-5,-3))
            player.take_damage(random.randint(3,10))
            return "I'm hungry, watch out I bite"

    def pet(self, player):
        """ Represents the act of the Tiger cat getting pet. Depending on the
        Tiger cats hunger level, the hunger level changes, and the cat may attack the player.
        Returns a string describing the cat. """
        if self._hunger >= 7:
            self.update_hunger(random.randint(-3,0))
            return "I love to be pet"
        elif self._hunger > 3 and self._hunger < 7:
            self.update_hunger(random.randint(-5,0))
            player.take_damage(random.randint(3,5))
            return "I was a little hungry I'm sorry if I bit you"
        elif self._hunger <= 3:
            self.update_hunger(random.randint(-5,0))
            player.take_damage(random.randint(3,10))
            return "If you pet me I will bite you, I'm hungry"

