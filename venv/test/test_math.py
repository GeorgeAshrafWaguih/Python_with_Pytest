"""
This module contains basic unit tests for math operations.
The purpose is to show how to use the pytest framework by example
"""

import pytest


# Basic test function
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


# Failed test
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


# Test verifies an exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

# Multiplication test ideas

# Two positive integers
# Identity: multiplying any number by 1
# zero: multiplying any number by zero
# positive by a negative
# negative by a negative
# multiply floats


def test_multiply_two_positive_ints():
    assert 2 * 3 == 6


def test_multiply_identity():
    assert 1 * 99 == 99


def test_multiply_zero():
    assert 0 * 100 == 0


# Parametrized test function
products = [
    (2, 3, 6),          # positive integers
    (1, 99, 99),        # identity
    (0, 99, 0),         # zero
    (3, -4, -12),       # positive by negative
    (-5, -5, 25),       # negative by negative
    (2.5, 6.7, 16.75)   # floats
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
