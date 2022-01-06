import pytest
@pytest.mark.one
def test_greater():
    num=10
    assert num > 9
@pytest.mark.one
def test_great_equal():
    num =20
    assert num >=15
@pytest.mark.one
def test_equal():
    num=10
    assert num==10

@pytest.mark.other
def test_less_than_equal():
    num =2
    assert num <=12