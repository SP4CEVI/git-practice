"""Арифметические операции калькулятора"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b
# rebase-demo 1


def power(a, b):
    """Возведение в степень"""
    return a ** b


def percent(value, pct):
    """Процент от числа"""
    return value * pct / 100
