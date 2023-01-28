import random
import door

class LockedDoor(door.Door):

  def __init__(self):
    '''Randomizes location of the key to one of 3 places.'''
    self._key_location = random.randint(1,3)
    self._input = 0


  def examine_door(self):
    '''Outputs message describing door'''
    return "You encounter a locked door, you must look around to find the key. "

  def menu_options(self):
    '''Outputs places to look for key.'''
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n"


  def get_menu_max(self):
    '''Returns number of options to choose from.'''
    return 3


  def attempt(self, option):
    '''User's attempt at unlocking door. First sets the input to the user's choice. Program then outputs the user's action
    Attributes:
    option(int) - User's choice of option.'''
    self._input = option
    if option == 1:  #Under the mat
      print("You look for the key under the mat.\n")
    elif option == 2: #Under the flower pot
      print("You look for the key under the flower pot.\n")

    elif option == 3:  #Under the fake rock
      print("You look for the key under the fake rock.\n")


  def is_unlocked(self):
    '''
    Once the input the user gave is equal to the spot the key was addressed to the door will be unlocked and moved on to the next door or finish the escape room.
    '''
    if self._input == self._key_location:
      return True
    else:
      return False

      
  def clue(self):
    '''
    When an inncorrect option is given by the user to where the key is hidden the user will be given this clue.
    '''
    return "Look somewhere else."

  def success(self):
    '''
    When the correect option is given by the user to where the key is hidden the user will be given this prompt.
    '''
    return "Congratulations, you opened the door."
