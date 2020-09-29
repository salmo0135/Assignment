"""
Group assignment
Taymoor
Ijaz
Luke

"""

from random import randrange
STARTING_POINT_OF_PLAYER = 'p' ;


class Maze:
    
    """ 
    Nested list created from file representing maze
    :param filename: file with maze on it
    :type filename: string
    
    :param _grid: nested list representing maze coordinates
    :type _grid: list
    
    """
    
    def __init__(self, _filename, _grid):
        self.file = open(_filename, 'r')
        self._grid = []
        line_list = []
        lines = self.file.readlines()
        for line in lines:
            line = line.strip('\n')
            line_list = [char for char in line]
            self._grid.append(line_list)
         #-- placing the player at the very start
        _grid[0][0] = STARTING_POINT_OF_PLAYER;

    #--- Rename the check method to can_move_to
    """
        if the location is a wall return False
        otherwise return True
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
        if self._grid[line_num][col_num] == "X":
            return False
        else:
            return True
        
    @classmethod
    def display(self):
        """
        Prints the grid on the screen
        """
        for line in self._grid:
            print("".join(line))

    @classmethod        
    def find_random_spot(self):
        """
        Finds a random open spot in the maze
        
        :return: coordinates for open spot
        :rtype: tuple
        """
        random_line_index = []
        random_col = 0
        random_col_index = 100
        
        while random_col != " ":
            random_line_index = randrange(len(self._grid))
            random_col_index = randrange(len(self._grid[random_line_index]))
            random_col = self._grid[random_line_index][random_col_index]
        
        coordinates = (random_line_index, random_col_index)
        return coordinates


    #--add random items
    """
        item = ['S','H','R','M']
        for i in item
            coordinates = find_random_spot()
            _grid(coordinates) = i
    """

    """
    def is_item(self):
        if self.grind[row][col] == randomItem:
            return True
        else:
            return False   
        
     """
    """
    
    """

    
            


