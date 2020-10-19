from math import sqrt


class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r, self.i * other.i)

    def __truediv__(self, other):
        return Complex(self.r / other.r, self.i / other.i)

    def __abs__(self):
        return sqrt(self.r**2 + self.i**2)

    def __str__(self):
        return str(self.r) + ' + ' + '(' + str(self.i) + ')' + '*j'


A = Complex(-1, -1)
B = Complex(-1, -1)
C = A + B
print(C)
D = A - B
print(D)
E = A * B
print(E)
F = A / B
print(F)
G = abs(A)
print(G)




