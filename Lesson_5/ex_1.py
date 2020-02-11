class Complex:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return '{:.2f}'.format(self.value + other.value)

    def __sub__(self, other):
        return '{:.2f}'.format(self.value - other.value)

    def __mul__(self, other):
        return '{:.2f}'.format(self.value * other.value)

    def __truediv__(self, other):
        return '{:.2f}'.format(self.value / other.value)

    def mod(self):
        return '{:.2f}'.format(complex(abs(self.value)))


C = complex(*[int(s) for s in input().split()])
D = complex(*[int(s) for s in input().split()])
C = Complex(C)
D = Complex(D)
print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(C.mod())
print(D.mod())