"""
maze.py - Group assignment
Taymoor
Ijaz
Luke
"""

from random import randrange
STARTING_POINT_OF_PLAYER = 'p'


class Maze:
    """ 
    Nested list created from text file representing a maze

    :param filename: text file containing maze
    :type filename: string
    """
    
    def __init__(self, _filename):
        """
        Initialization of instance attributes
        """
        # -- open text file containing maze
        self.file = open(_filename, 'r')
        self._grid = []
        # -- initialize line_list and append into list
        line_list = []
        lines = self.file.readlines()
        for line in lines:
            line = line.strip('\n')
            line_list = [char for char in line]
            self._grid.append(line_list)
         # -- placing the player at the very start
        self._grid[6][0] = STARTING_POINT_OF_PLAYER
        
        

    # --- Rename the check method to can_move_to
        """ 
        :return: return False if the location is a wall, otherwise return True
        :rtype: bool
        """

    #--@classmethod doesnt need to be a class method likewise for every other class method
    def can_move_to(self, line_num, col_num):
        """
        Check if coordinate is an empty space or wall

        :param line_num: establishes line number in grid
        :type line_num: integer
        
        :param col_num: establishes column number in grid
        :type col_num: integer
        
        :return: False if coordinates are a wall, True if empty space
        :rtype: bool
        """
        # -- checks if the coordinate is an empty space
        if self._grid[line_num][col_num] == "X":
            return False
        else:
            return True
        
    def display(self):
        """
        Prints the grid on the screen
        """
        for line in self._grid:
            print("".join(line))


    def find_random_spot(self):
        """
        Finds a random open spot in the maze
        
        :return: coordinates for open spot
        :rtype: tuple
        """
        random_line_index = []
        random_col = 0
        random_col_index = 100

        # -- loops through maze and stops when it finds an open spot
        while random_col != " ":
            random_line_index = randrange(len(self._grid))
            random_col_index = randrange(len(self._grid[random_line_index]))
            random_col = self._grid[random_line_index][random_col_index]
        # -- returns the coordinates of the open spot
        coordinates = (random_line_index, random_col_index)
        return coordinates

    @property
    def grid(self):
        return self._grid

    #--add random items
    
    @grid.setter
    def grid(self, value):
        self._grid = value
    
    def add_items(self):
        """
        Adds random items to the maze
        """
        # -- item list
        item = ['S','H','R','M']
        # -- loops through item list and adds them to the maze
        for i in item:
            x_coordinate, y_coordinate = self.find_random_spot()
            self.grid[x_coordinate][y_coordinate] = i
            print(x_coordinate, y_coordinate)
        print(self._grid)


   
    def is_item(self, x_coordinate, y_coordinate):
        """
        If the location requested is a random item, return True

        :param x_coordinate: x coordinate of the location requested
        :type x_coordinate: integer

        :param y_coordinate: y coordinate of the location requested
        :type y_coordinate: integer

        :return: return False if the location requested is not a random item, else return True
        :rtype: bool
        """
        if self.grid[x_coordinate][y_coordinate] == "X" or self.grid[x_coordinate][y_coordinate] == " ":
            return False
        else:
            return True
        
    
