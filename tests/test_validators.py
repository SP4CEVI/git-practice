"""Unit-тесты проверки ввода"""
from validators import is_number, is_operation, is_positive


def test_is_number():
    assert is_number("3.14")
    assert not is_number("abc")

def test_is_operation():
    assert is_operation("+")
    assert not is_operation("x")

def test_is_positive():
    assert is_positive(5)
    assert not is_positive(-1)
