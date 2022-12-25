"""
This module contains basic unit tests for math operations.
The purpose is to show how to use the pytest framework by example
"""


# Basic test function
def test_one_plus_one():
    assert 1 + 1 == 2


# Failed test
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c
