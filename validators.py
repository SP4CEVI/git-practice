"""Проверка ввода пользователя"""


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def is_operation(text):
    return text in ("+", "-", "*", "/")


def is_positive(value):
    """Проверяет, что число положительное"""
    return value > 0
