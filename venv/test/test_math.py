"""
This module contains basic unit tests for math operations.
The purpose is to show how to use the pytest framework by example
"""

import pytest

# Basic test function
def test_one_plus_one():
    assert 1 + 1 == 2


# Failed test
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


# Test verifies an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)
