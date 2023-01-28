import random
import entity


class Dragon(entity.Entity):
    """
    Sets the type of attack the dragon uses
    """
    def basic_attack(self, hero):
        """Returns the type of attack(basic) in a string format"""
        # the hero takes a random amount of damage from the sword attack
        tail_attack = random.randrange(3, 7)
        hero.take_damage(tail_attack)
        return "\n" + self.name + " smashed you with its tail " + "for " + str(tail_attack) + " damage"

    def special_attack(self, hero):
        """Returns the type of attack(special) in a string format"""
        # the hero takes a random amount of damage from the sword attack
        claw_attack = random.randrange(4, 8)
        hero.take_damage(claw_attack)
        return "\n" + self.name + " smashed you with its claw " + "for " + str(claw_attack) + " damage"

