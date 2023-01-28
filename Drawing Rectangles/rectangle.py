class Rectangle:
    """
    This class creates the width and height attributes and all the necessary functions

    Attributes: – x, y, width, height : represents the cordinates and the width and height of the grid
    """

    def __init__(self, w, h):
        """
        This function takes the value of the width and height from the user

        Arguments: (w): width
                  (h): height
        """
        self.width = w
        self.height = h
        self.x = 0
        self.y = 0

    def get_coords(self):
        """This function returns the x and y values as a pair."""
        return self.x, self.y

    def get_width(self):
        """
        This function returns the rectangle’s width. 
        """
        return self.width

    def get_height(self):
        """ moves the rectangle up one row. """
      
        return self.height

    def move_up(self):
        """moves the rectangle down one row. """
        self.y -= 1

    def move_down(self):
        """moves the rectangle left one column. """
        self.y += 1

    def move_left(self):
        self.x -= 1
        

    def move_right(self):
        """moves the rectangle right one column. """
        self.x += 1

        
