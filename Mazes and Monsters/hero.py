import entity
import random


class Hero(entity.Entity):

  def __init__(self, name):
    # intializes max_hp using super, sets the hero's starting location to row = 0 col = 0
    super().__init__(name, 25)
    self._loc = [0, 0]
    #row, column

    
  def attack(self, entity):
    """
    Hero attack enemy. randomize damage towards enemy.
    """
    
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return f"{self._name} attacks a {entity._name} for {dmg} damage."

  
  def go_north(self):
    """
    Updating location of hero by subtracting 1 from the row

    if the user wants to going out of bounds, it will return "x"
    """
    
    if self._loc[0] > 0:
      self._loc[0] = self._loc[0] - 1
    else:
      return "x"

  
  def go_south(self):
    """
    Updating location of hero by adding 1 to the row

    if the user wants to going out of bounds, it will return "x"
    """
    if self._loc[0] < 4:
      self._loc[0] = self._loc[0] + 1
    else:
      return "x"

  
  def go_east(self):
    """
    Updating location of hero by subtracting 1 from the column

    if the user wants to going out of bounds, it will return "x"
    """
    if self._loc[1] > 0:
      self._loc[1] = self._loc[1] - 1

    else:
      return "x"

  
  def go_west(self):
    """
    Updating location of hero by adding 1 to the column

    if the user wants to going out of bounds, it will return "x"
    """
    
    if self._loc[1] < 4:
      self._loc[1] = self._loc[1] + 1
    else:
      return "x"