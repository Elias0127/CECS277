class Map:
  _instance = None
  _initialized = False

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  
  def __init__(self):
    """
    Create 2D list from the text file. The map has the content of the file. A revealed list is used to see if the contents are diplayed or not
    """
    
    if not Map._initialized:
      self._map = []
      self._revealed = []
      Map._initialized = True
      with open('map.txt') as f:
        lines = f.readlines()
        for x in range(len(lines)):
          string = lines[x].strip()
          self._map.append([])
          self._revealed.append([])
          for y in range(len(string)):
            self._map[x].append(string[y])
            self._revealed[x].append(False)

  
  def __getitem__(self, row):
    """
    return specified row from map
    """
    
    return self._map[row]

  
  def __len__(self):
    """
    return number of rows in the map
    """
    
    return len(self._map)

  
  def show_map(self, loc):
    """
    Display the map in a 5x5 matrix, with "x" for unrevealed locations and "*" for hero's location
    """
    
    map_string = ""
    for x in range(len(self._map)):
      for y in range(len(self._map[x])):
        if x == loc[0] and y == loc[1]:
          map_string += "*"
        elif self._revealed[x][y] == True:
          map_string += self._map[x][y]
          
        else:
          map_string += "x"
      map_string += "\n"

    return map_string


  def reveal(self, loc):
    """
    Set value in 2D list of the specified location to True
    """
    
    self._revealed[loc[0]][loc[1]] = True

  
  def remove_at_loc(self, loc):
    """
    Change the value in the 2D list of the specified location to be "n"
    """
    
    self._map[loc[0]][loc[1]] = "n"