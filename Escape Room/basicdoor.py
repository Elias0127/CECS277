import random
import door

class BasicDoor(door.Door):
  '''
  A basic door that can either be pushed or pulled open. State of door is randomized at the beginning, unlocks when the user guesses the correct state. 
  '''
  def __init__(self):
    self._state = random.randint(1,2)
    self._input = 0

  def examine_door(self):
    return "You encounter a basic door, you can either push it or pull it to open."

  def menu_options(self):
    return "1. Push\n2. Pull\n"


  def get_menu_max(self):
    '''Returns number of menu options'''
    return 2


  def attempt(self, option):
    '''User's attempt at unlocking door. First sets the input to the user's choice. Program then outputs the user's action
    Attributes:
    option(int) - User's choice of option.
    '''
    self._input = option
    if option == 1:  #Push
      print("You push the door.\n")
    else:     #Pull
      print("You pull the door.\n")

  def is_unlocked(self):
    '''Determines whether door has been opened or not by checking if the state matches with user's input. 
    Returns a boolean value.'''
    if self._input == self._state:  #choose correct option
      return True
    else:
      return False

      
  def clue(self):
    '''Message that helps user pick the correct option. '''
    return "Try the other way."


  def success(self):
    '''Outputs message if user successfully opens door'''
    
    return "Congratulations, you opened the door."




  