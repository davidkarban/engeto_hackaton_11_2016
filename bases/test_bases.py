from bases import *
import pytest

def test_converts():
    assert(decimal_to_binary(130)) == "10000010"
    assert(binary_to_decimal("10000010")) == 130

    # convert
    assert(convert_to_decimal("0",10)) == 0
    assert(convert_to_decimal("FFFF",16)) == 65535
    assert(convert_to_decimal("100",16)) == 256

@pytest.parametrize("decimal", [10,20,30])
@pytest.parametrize("base", [2,10])
def test_converts(decimal, base):
    assert(convert_to_decimal("100",16)) == 256

