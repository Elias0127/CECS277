import entity
import random 

class Enemy(entity.Entity):

  def __init__(self):
    """
    randomize a name from a list of enemy names and randomize their health 
    """
    
    bad_guy = ["Goblin", "Troll", "Ghoul", "Skeleton", "Kobold"]
    #self._name = random.choice(bad_guy)
    #self._hp = random.randint(4,8)
    
    super().__init__(random.choice(bad_guy), random.randint(4,8))

  
  def attack(self, entity):
    """
    Enemy attacks the hero. randomize damage towards hero. Hero should take the damage.
    """
    
    dmg = random.randint(1, 4)
    entity.take_damage(dmg)
    return f"{self._name} attacks {entity._name} for {dmg} damage."