class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


x = input('введите делимое число ')
y = input('введите делитель ')

try:
    x = int(x)
    y = int(y)
    if y == 0:
        raise OwnError("на ноль делить нельзя")
except ValueError:
    print("вы ввели не число")
except OwnError as err:
    print(err)
else:
    res = x/y
    print(f'ответ - {res}')
