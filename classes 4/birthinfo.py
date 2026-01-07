from datetime import date
from typing import Union, List, Tuple


class BirthInfo:
    def __init__(self, birth_date: Union[date, str, List[int], Tuple[int, int, int]]):
        try:
            if isinstance(birth_date, date):
                self.birth_date = birth_date
            elif isinstance(birth_date, str):
                self.birth_date = date.fromisoformat(birth_date)
            elif isinstance(birth_date, (list, tuple)) and len(birth_date) == 3:
                year, month, day = birth_date
                self.birth_date = date(year, month, day)
            else:
                raise TypeError
        except (ValueError, TypeError):
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self) -> int:
        today = date.today()

        age_years = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age_years -= 1

        return age_years