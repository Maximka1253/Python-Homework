import math
x = float(input('x первого вектора: '))
y = float(input('y первого вектора: '))
x1 = float(input('x второго вектора: '))
y1 = float(input('y второго вектора: '))
class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # 1. Длина вектора
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    # 2. Угол наклона относительно положительного направления оси X (в радианах)
    def angle(self):
        return math.atan2(self.y, self.x)

    # 3. Сложение векторов
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # 4. Вычитание векторов
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # 5. Скалярное произведение
    def dot(self, other):
        return self.x * other.x + self.y * other.y
v1 = Vector(x, y)
v2 = Vector(x1, y1)
print('--------------------------','\nv1 = ', v1, '\nv2 = ', v2, "\nДлина v1:", v1.length(), "\nДлина v2:", v2.length(), "\nУгол v1 (рад):", v1.angle(), "\nУгол v2 (рад):", v2.angle(),"\nСумма:", v1 + v2,"\nРазность:", v1 - v2,"\nСкалярное произведение: ", v1.dot(v2))