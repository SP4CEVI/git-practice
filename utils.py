"""Вспомогательные функции"""


def format_result(value):
    """Красиво форматирует результат: 5.0 -> 5"""
    return int(value) if float(value).is_integer() else value
# merge-demo 1
# merge-demo 2
