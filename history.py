"""История вычислений"""

history = []


def remember(expression, result):
    history.append(f"{expression}={result}")


def show():
    for line in history:
        print(line)
