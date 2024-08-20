import pytest
from add_subtract import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(1) == 1
    assert add(y=2) == 2
    assert add() == 0
    assert add(-1, -2) == -3

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1) == 1
    assert subtract(y=2) == -2
    assert subtract() == 0
    assert subtract(-1, -2) == 1
