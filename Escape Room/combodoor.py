import door
import random

class ComboDoor(door.Door):
  '''
  A door programmed to have a random number be the key to open the door. A clue indicating if the users guess was higher or lower than the actual number will be given each guess.  
  '''
  def __init__(self):
    '''Correct value is randomized to a number between 1-10. Input '''
    self._correct_value = random.randint(1,10)
    self._input = 0

  def examine_door(self):
    return "You encounter a door with a combination lock. You can spin the dial to a number 1-10."

  def menu_options(self):
    return "Enter a number (1-10): "

  def get_menu_max(self):
    return 10


  def attempt(self, option):
    '''User's attempt at unlocking door. First sets the input to the user's choice. Program then outputs the user's action
    Attributes:
    option(int) - User's choice of option.'''
    self._input = option
    print(f"You turn the dial to ... {option}\n")
      

  def is_unlocked(self):
    '''Determines whether door has been opened or not by checking if the state matches with user's input. 
    Returns a boolean value.'''
    if self._input == self._correct_value:
      return True
    else:
      return False
      

      
  def clue(self):
    '''Message that helps user pick the correct option. Tells user if their input was higher or lower than the correct value.'''
    if self._input > self._correct_value:
      return "Try a lower number."
    else:
      self._input < self._correct_value
      return "Try a higher number."


  def success(self):
    '''
    After guessing the correct number the user will be prompted with this message.
    '''
    return "Congratulations, you found the correct value and opened the door."