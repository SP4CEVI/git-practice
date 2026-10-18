from config import APP_NAME, VERSION
from operations import add, subtract, multiply, divide

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    print(f"{APP_NAME} v{VERSION}")
    a = float(input("Первое число: "))
    op = input("Операция (+-*/): ")
    b = float(input("Второе число: "))
    print("Результат:", round(OPERATIONS[op](a, b), 4))


if __name__ == "__main__":
    main()
