
class Map:
    """ Map is a Singleton class, so there is only ever one instance of the class Map.
    Contains an _instance variable for checking if there is an instance of the class, and
    _initialized variable for initializing the map.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args):
        """ New method overrides the Maps object class new method by making enabling the
        Map class to only ever create 1 instance of the Map class.
        """
        # if there is no instance of the Map class create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        # return the instance
        return cls._instance

    def load_map(self, map_num):
        """ Load map constructs the map depending on which file it reads. """
        # either opens map 1,2, or 3
        if map_num == 1:
            self._file = open("map.txt")
        if map_num == 2:
            self._file = open("map2.txt")
        if map_num == 3:
            self._file = open("map3.txt")

        # nested for loop constructing a 2D list with the contents from the open file
        self._map = []
        for self._row in self._file:
            self._characters = self._row.strip()
            self._map2 = []
            for self._column in self._characters:
                self._map2.append(self._column)
            self._map.append(self._map2)

        # nested for loop constructing a 2D list appended with False values
        self._revealed = []
        for self._row in range(5):
            self._revealed2 = []
            for self._column in range(5):
                self._revealed2.append(False)
            self._revealed.append(self._revealed2)

    def __init__(self):
        """ Init method initializes the map with the map.txt file. """
        if not Map._initialized:
            self.load_map(1) # calls load map, initializes with map.txt file
        Map._initialized = True # states that an instance has been initialized

    def __getitem__(self, row):
        """ Overrides the [] operator, enabling the map to return the location of the
        hero.
        """
        return self._map[row]

    def __len__(self):
        """ Overrides the len() operator, by returning the length of the map. """
        return len(self._map)

    def show_map(self, loc):
        """ Show map method fills and displays the map as a string."""
        m = "" # map as a string
        # nested for loop iterating through the rows and columns of the map
        for row, letters in enumerate(self._map):
            for column, letter in enumerate(letters):
                # if the location on the map is equal to heroes location concatenate a '*'
                if row == loc[0] and column == loc[1]:
                    m += "*"
                # if the location on the map == False denoting it hasn't been visited concatenate an 'x'
                elif self._revealed[row][column] == False:
                    m += "x"
                # otherwise concatenate on the location of the map
                else:
                    m += self._map[row][column]
            m += "\n"
        return m # return the map as a string

    def reveal(self, loc):
        """ Reveal method sets the locations revealed value to True, denoting the hero
        has visited that location.
        """
        self._revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self, loc):
        """ Remove At Location method removes contents at the specified location on the map,
        and replaces it with an 'n'.
        """
        self._map[loc[0]][loc[1]] = "n"