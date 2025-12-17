import math

class Shape3D:
    def volume(self):
        pass

    def surface_area(self):
        pass

    def get_name(self):
        return self.__class__.__name__

class Cube(Shape3D):
    def __init__(self, a):
        self.a = a

    def volume(self):
        return self.a ** 3

    def surface_area(self):
        return 6 * (self.a ** 2)

class Sphere(Shape3D):
    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)

    def surface_area(self):
        return 4 * math.pi * (self.r ** 2)


class Cylinder(Shape3D):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return math.pi * (self.r ** 2) * self.h

    def surface_area(self):
        return 2 * math.pi * self.r * (self.h + self.r)

class Parallelepiped(Shape3D):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def surface_area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)


class Ellipsoid(Shape3D):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c

    def surface_area(self):
        p = 1.6075
        part = ((self.a ** p * self.b ** p) + (self.a ** p * self.c ** p) + (self.b ** p * self.c ** p)) / 3
        return 4 * math.pi * (part ** (1 / p))

def analyze_figures(figures):

    total_volume = sum(f.volume() for f in figures)
    huge_figures = []

    print(f"{'ФИГУРА':<15} | {'ОБЪЕМ (V)':<15} | {'ПЛОЩАДЬ (S)':<15}")
    print("-" * 50)

    for f in figures:
        v = f.volume()
        s = f.surface_area()

        print(f"{f.get_name():<15} | {v:<15.2f} | {s:<15.2f}")

        if v >= (total_volume - v):
            huge_figures.append(f)

    print("-" * 50)
    print(f"Суммарный объем всех фигур: {total_volume:.2f}")
    print("-" * 50)

    if huge_figures:
        for hf in huge_figures:
            print(f"Фигура, превышающая остальные: {hf.get_name()} (V = {hf.volume():.2f})")
    else:
        print("РЕЗУЛЬТАТ ПОИСКА: Фигур, объем которых больше суммы остальных, не найдено.")

if __name__ == "__main__":

    shapes = [
        Cube(3),  # a=3
        Sphere(2),  # r=2
        Cylinder(2, 5),  # r=2, h=5
        Parallelepiped(10, 15, 10),  # Огромная фигура
        Ellipsoid(4, 2, 3)  # a=1, b=2, c=3
    ]

    analyze_figures(shapes)