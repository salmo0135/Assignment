"""
Group assignment
Taymoor
Ijaz
Luke

"""

from random import randrange


class Maze:
    def __init__(self, _filename, _grid):
        self.file = open(_filename, 'r')
        self._grid = []
        line_list = []
        lines = self.file.readlines()
        for line in lines:
            line = line.strip('\n')
            line_list = [char for char in line]
            self._grid.append(line_list)
            

    def check(self, line_num, col_num):
        if self._grid[line_num, col_num] == "X":
            return False
        else:
            return True
        

    def display(self):
        for line in self._grid:
            print("".join(line))

    def find_random_spot(self):
        random_line_index = []
        random_col = 0
        random_col_index = 100
        
        while random_col != "*":
            random_line_index = randrange(len(self._grid))
            random_col_index = randrange(len(self._grid[random_line_index]))
            random_col = self._grid[random_line_index][random_col_index]
        
        coordinates = (random_line_index, random_col_index)
        
    
            


