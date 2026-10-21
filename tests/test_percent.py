"""Тест новой функции percent()"""
from operations import percent


def test_percent():
    assert percent(200, 15) == 30


def test_percent_zero():
    assert percent(500, 0) == 0
