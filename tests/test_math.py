def add(a,b):
    return a+b


def square(x):
    return x * x

def test_negative_numbers():
    assert add(-6,5) == -1

def test_add():
    assert add(2,3) == 5

def test_square_positive():
    assert square(5)==25


def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16