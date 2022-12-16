from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(Number: int) -> int:
    """Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number: int) -> int:
    """Проверка вводимого значения"""
    if your_number <= 0:
        return
    sq: int = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {sq}')


print(message)
calc(25.5)
