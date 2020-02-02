class Compl_did():
    def __init__(self, x):
        self.x = x #complex(x)
        #self.y = y
        

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x

com_1 = Compl_did(complex(1, 2))
com_2 = Compl_did(complex(2, 3))
print(com_1.x)
print(com_2.x)

print(com_1 + com_2)
print(com_1 * com_2)

