class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


x = None
y = []
while x != 'q':
    x = input('введите число ')
    if x == 'q':
            print("программа завершена")
            break
    try:
        
        if not x.isdigit():
            raise OwnError("вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        y.append(x)
        print(f'ваш список - {y}')
