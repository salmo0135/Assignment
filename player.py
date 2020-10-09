"""
player.py - Group assignment
Taymoor
Ijaz
Luke
"""

backpack = []

class Player:
    """
    Contains an attribute named backpack that will store the random items picked up
    :param_ _backpack: Object used to store random items
    :rtype: object
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialization of instance attributes
        """
        self._backpack = []
        self._x = x_coordinate
        self._y = y_coordinate
        pass
