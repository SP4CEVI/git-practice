"""История вычислений"""

history = []


def remember(expression, result):
    history.append(f"{expression}={result}")
