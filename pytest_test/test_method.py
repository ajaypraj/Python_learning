import pytest


@pytest.fixture
def input_value():
    input_val = 39
    return input_val


def test_division_test(input_value):
    assert input_value % 3 == 0
