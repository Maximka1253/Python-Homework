class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.calories = (self.fats * 4 + self.carbohydrates * 4 + self.fats * 9) #примерный подсчет каллорий

    def __repr__(self):
        return f"FoodInfo({self.calories}, {self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(self.proteins + other.proteins,
                        self.fats + other.fats,
                        self.carbohydrates + other.carbohydrates)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(self.proteins * other,
                        self.fats * other,
                        self.carbohydrates * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(self.proteins / other,
                        self.fats / other,
                        self.carbohydrates / other)

    def __floordiv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return FoodInfo(self.proteins // other,
                        self.fats // other,
                        self.carbohydrates // other)

    def __rmul__(self, other):
        return self.__mul__(other)

f1 = FoodInfo(20, 12, 56)
f2 = FoodInfo(5, 31, 73)

print(f1 + f2)
print(f1 * 2)
print(3 * f2)
print(f1 / 2)
print(f1 // 3)