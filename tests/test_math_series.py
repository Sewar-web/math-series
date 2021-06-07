from math_series import __version__
import math_series
from math_series.math_series import fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_one_it():
    assert fibonacci(3)==2

def test_two_it():
    assert fibonacci(5)==5


def test_three_it():
    assert lucas(1)==1


def test_four_it():
    assert lucas(2)==3


def test_five_it():
    assert lucas(3)==4