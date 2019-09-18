import pytest

def simple_function(is_it_true):
    return is_it_true

def simple_wrong_function(is_it_true):
    return not is_it_true

def test_simple_function():
    assert simple_function(True) == True

def test_simple_wrong_function():
    assert simple_wrong_function(True) == True
