class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = 'strict'

class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = 'kind'

# Дочь наследует методы обоих родителей. 
# Mother стоит первой, чтобы greet() вернул "Hi, honey!"
class Daughter(Mother, Father):
    pass

# Проверка
d = Daughter()
print(f"Начальное настроение: {d.mood}")
print(f"Приветствие: {d.greet()}")  # Из Mother

d.be_strict()  # Из Father
print(f"Настроение после be_strict: {d.mood}")

d.be_kind()    # Из Mother
print(f"Настроение после be_kind: {d.mood}")