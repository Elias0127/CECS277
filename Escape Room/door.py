import abc

class Door(abc.ABC):


  @abc.abstractmethod
  def examine_door(self):
    '''
    abstract for each different door we programmed a message to give the user an understand of what type of door it is.
    '''
    pass

  @abc.abstractmethod
  def menu_options(self):
    '''
    abstract for the options that each door possesses.
    '''
    pass
    
  @abc.abstractmethod
  def get_menu_max(self):
    '''
    abstract for the max values of each door.
    '''
    pass

  @abc.abstractmethod
  def attempt(self, option):
    '''
    abstract for each attempt the user inputs for the codes to unlock each door.
    '''
    pass
    
  @abc.abstractmethod
  def is_unlocked(self):
    '''
    abstract for each door being unlocked by the correct code.
    '''
    pass
    
  @abc.abstractmethod
  def clue(self):
    '''
    abstract for each door to output a clue for when an inncorrect guess is given.
    '''
    pass

  @abc.abstractmethod
  def success(self):
    '''
    abstract for when the door is successfully opened by the correct code for each door.
    '''
    pass