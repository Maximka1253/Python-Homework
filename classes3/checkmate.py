from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, target_h, target_v):
        pass

    def _get_coords(self, h, v):
        # Вспомогательный метод для перевода 'a'-'h' в 1-8
        letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return letters[h], v

class King(ChessPiece):
    def can_move(self, target_h, target_v):
        curr_h_num, curr_v = self._get_coords(self.horizontal, self.vertical)
        targ_h_num, targ_v = self._get_coords(target_h, target_v)
        
        # Король ходит на 1 клетку в любом направлении
        delta_h = abs(curr_h_num - targ_h_num)
        delta_v = abs(curr_v - targ_v)
        
        return (delta_h <= 1 and delta_v <= 1) and not (delta_h == 0 and delta_v == 0)

class Knight(ChessPiece):
    def can_move(self, target_h, target_v):
        curr_h_num, curr_v = self._get_coords(self.horizontal, self.vertical)
        targ_h_num, targ_v = self._get_coords(target_h, target_v)
        
        delta_h = abs(curr_h_num - targ_h_num)
        delta_v = abs(curr_v - targ_v)

        return (delta_h == 2 and delta_v == 1) or (delta_h == 1 and delta_v == 2)

# Проверка
king = King('e', 1)
knight = Knight('c', 3)

moves_to_test = [('e', 2), ('d', 2), ('f', 3), ('b', 5)]

print("Проверка Короля (e1):")
for h, v in moves_to_test:
    print(f"Ход в {h}{v}: {king.can_move(h, v)}")

print("\nПроверка Коня (c3):")
for h, v in moves_to_test:
    print(f"Ход в {h}{v}: {knight.can_move(h, v)}")