import pytest
from addition import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-5, -5) == -10
    assert addition(100, 200) == 300

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 0) == 0   
    assert subtraction(10, 5) == 5