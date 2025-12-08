class User:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str) or not name or not name.isalpha():
            raise ValueError("Некорректное имя")
        self.__name = name

        # Валидация возраста при создании
        if not isinstance(age, int) or not (0 <= age <= 110):
            raise ValueError("Некорректный возраст")
        self._age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str) or not new_name or not new_name.isalpha():
            raise ValueError("Некорректное имя")
        self.__name = new_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError("Некорректный возраст")
        self._age = new_age