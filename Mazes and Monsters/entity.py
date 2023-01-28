import abc

class Entity(abc.ABC):

  def __init__(self, name, max_hp):
    self._name = name
    self._max_hp = max_hp
    self._hp = self._max_hp

  
  @property 
  def name(self):
    #returns object name 
    return self._name

  
  @property 
  def hp(self):
    #returns max Hp
    return self._hp

  
  def take_damage(self, dmg):
    """
    Subtracts damage from Hp and Hp isn't allowed to drop below 0
    """
    
    self._hp = self._hp - dmg 
    if self._hp < 0:
      self._hp = 0

  
  def heal(self):
    #hp is reset to max_hp
    self._hp = self._max_hp

  
  def __str__(self):
    #format "Name\nHP: hp/max_hp"
    return f"{self._name} \nHP: {self._hp}/{self._max_hp}"

  
  @abc.abstractmethod
  def attack(self, entity):
    """
    all entity subclasses will override to attack and do damage to the opposing entity 
    """
