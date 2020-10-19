from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def constructor(cls, line):
        g = line.split(sep=', ')
        g0 = line[0]
        g1 = line[3]
        g2 = line[6]
        return cls(g0, g1, g2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self):
        return "Вектор с координатами" + ' ' + '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def __repr__(self):
        return self.__str__()

    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)


def area(a, b):
    return sqrt(a.x**2 + a.y**2)*sqrt(b.x**2 + b.y**2)*sqrt(1 - (a.x*b.x + a.y*b.y)/(sqrt(a.x**2 + a.y**2)*sqrt(b.x**2 + b.y**2)))


def par_volume(a, b, c):
    return abs(a.x*(b.y*c.z - b.z*c.y) - a.y*(b.x*c.z - c.x*b.z) + a.z*(b.x*c.y - b.y*c.z))


def centre_mass(a, b, c):
    return Vector((a.x + b.x + c.x)/3, (a.y + b.y + c.y)/3, (a.z + b.z + c.z)/3)


a = Vector(1, 2, 3)
print(a)
s = Vector.constructor('4, 8, 7')
print(s)
b = Vector(3, 5, 7)
c = area(a, b)
print(c)
d = Vector(3, 4, 5)
f = par_volume(a, b, d)
print(f)

vectors = []
for i in range(3):
    prom = input().split()
    vectors.append(Vector(int(prom[0]), int(prom[1]), int(prom[2])))

result = sorted(vectors, key=lambda vector: vector.length())
print('Максимальное расстояние от начала координат:' + str(result[-1]))


m = centre_mass(a, b, d)
print('Центр масс:', m)





