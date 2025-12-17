class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self): return self.__name

    def get_price(self): return self.__price

    def get_weight(self): return self.__weight

    def set_name(self, name): self.__name = name

    def set_price(self, price): self.__price = price

    def set_weight(self, weight): self.__weight = weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = self.get_price() * quantity
        self.__total_weight = self.get_weight() * quantity

    def get_quantity(self): return self.__quantity

    def get_total_price(self): return self.__total_price

    def get_total_weight(self): return self.__total_weight

    def set_quantity(self, quantity):
        self.__quantity = quantity
        self.__total_price = self.get_price() * quantity
        self.__total_weight = self.get_weight() * quantity


class Check(Buy):
    def print_check(self):
        print(f"Товар: {self.get_name()}")
        print(f"Цена за ед.: {self.get_price()} | Вес за ед.: {self.get_weight()}")
        print(f"Кол-во: {self.get_quantity()}")
        print(f"Цена покупки: {self.get_total_price()}")
        print(f"Вес покупки:  {self.get_total_weight()}")

receipt = Check(name="Ноутбук", price=45000, weight=1.7, quantity=3)
receipt.print_check()