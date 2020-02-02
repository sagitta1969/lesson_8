# оргтехника
class Org_tex:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Printer(Org_tex):
    def __init__(self, name, price, param_printer):
        super().__init__(self, name, price)


class Scanner(Org_tex):
    def __init__(self, name, price, param_scanner):
        super().__init__(self, name, price)

class Xerox(Org_tex):
    def __init__(self, name, price, param_xerox):
        super().__init__(self, name, price)


#склад
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehaus:
    unit = {'pr': 0, 'sk': 0, 'xr': 0}
    def __init__(self):
        pass
        #self.unit = unit
    
    def doc_prihod(self):
        print("документ прихода")
        try:
            x = int(input("введите число принтеров "))
            y = int(input("введите число сканеров "))
            z = int(input("введите число ксероксов "))
            if x < 0 or y < 0 or z < 0:
                raise OwnError("вы ввели отрицательное число")
        except ValueError:
            print('не число')

        except OwnError as err:
            print(err)

        print(f"В документе:\nпритеров - {x}\nсканеров - {y}\nксероксов - {z}")
        q = [x, y, z]
        print("приём оргтехники на склад")
        Warehaus.unit['pr'] += q[0]
        Warehaus.unit['sk'] += q[1]
        Warehaus.unit['xr'] += q[2]
        return f"итого количество: принтетов - {Warehaus.unit['pr']}, сканеров - {Warehaus.unit['sk']}, ксероксов - {Warehaus.unit['xr']}"
    
    def doc_rashod(self):
        print("передача оргтехники в подразделения")
        try:
            x = int(input("введите число принтеров "))
            if x < 0 or x > Warehaus.unit['pr']:
                raise OwnError("вы ввели не корректные данные")
            y = int(input("введите число сканеров "))
            if y < 0 or y > Warehaus.unit['sk']:
                raise OwnError("вы ввели не корректные данные")
            z = int(input("введите число ксероксов "))
            if z < 0 or z > Warehaus.unit['xr']:
                raise OwnError("вы ввели не корректные данные")
                
        except ValueError:
            print('не число')

        except OwnError as err:
            print(err)

        print(f"В документе:\nпритеров - {x}\nсканеров - {y}\nксероксов - {z}")
        r = [x, y, z]
        print("отгрузка оргтехники в подразделение")
        Warehaus.unit['pr'] -= r[0]
        Warehaus.unit['sk'] -= r[1]
        Warehaus.unit['xr'] -= r[2]
        return f"на складе осталось: принтетов - {Warehaus.unit['pr']}, сканеров - {Warehaus.unit['sk']}, ксероксов - {Warehaus.unit['xr']}"


doc_1 = Warehaus()
#w.doc_prihod()
print(doc_1.doc_prihod())
print(Warehaus.unit)

doc_2 = Warehaus()
print(doc_2.doc_rashod())
