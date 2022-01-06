import pytest
import math


def test_sqrt():
    num = 25
    assert 5 == math.sqrt(num)

def test_square():
    num=7
    assert 7*7==40

def testequality():
    assert 10==12
