import random
import entity


class Hero(entity.Entity):
    """Sets the player's weapon to attack the dragon """
    def sword_attack(self, dragon):
        """Returns the type of weapon(sword) in a string format"""
        # The dragon takes a random amount of damage from the sword attack
        sword_damage = random.randrange(1, 6) + random.randrange(1, 6)
        dragon.take_damage(sword_damage)
        return "\n" + self.name + " slashed " + dragon.name + " for " + str(sword_damage) + " damages"

    def arrow_attack(self, dragon):
        """Returns the type of weapon(arrow) in a string format"""
        # The dragon takes a random amount of damage from the arrow attack
        arrow_damage = random.randrange(1, 12)
        dragon.take_damage(arrow_damage)
        return "\n" + self.name + " hit " + dragon.name + " for " + str(arrow_damage) + " damages"
