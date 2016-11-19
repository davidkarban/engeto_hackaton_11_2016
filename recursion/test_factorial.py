from factorial import *
import pytest

def test_factorial():
    assert(factorial(5)) == 120
    assert(factorial(1)) == 1

