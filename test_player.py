import pytest
from player import Player

@pytest.fixture
def player():
    return Player(0,1)


def test_constructor(player):
    """
    This will test the constructor for valid return types
    """
    assert player._x == 0
    assert player._y == 1
    assert player._backpack == []


def test_backpack(player):
    """
    test the backpack property
    """
    assert type(player.__class__.backpack) == property

def test_backpack_length(player):
    """
    Test to see correct return value
    """
    assert len(player.backpack) == 0

def test_adding_to_backpack(player):
    """
    testing the setter for backpack
    """
    player.backpack = 'x'
    assert player.backpack[0] =='x'
    assert len(player.backpack) == 1

def test_x(player):
    """
    test that x co-ordinate has a property
    """
    assert type(player.__class__.x) == property

def test_x_property(player):
    """
    test for correct return value of getter
    """
    assert player.x == 0

def test_setter_x(player):
    """
    test the setter for x
    """
    player.x = 1
    assert player.x == 1


def test_y_value(player):
    """
    test y has a getter
    """
    assert type(player.__class__.y) == property

def test_y_property(player):
    """
    test correct return values for y getter
    """
    assert player.y == 1

def test_setter_y(player):
    """
    test the setter for y co-ordinate
    """
    player.y = 2
    assert player.y == 2
