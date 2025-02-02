class Book:
    """Базовый класс книги."""

    def _init_(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def _str_(self):
        return f"Книга {self.name}. Автор {self.author}"

    def _repr_(self):
        return f"{self._class.name_}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга."""

    def _init_(self, name: str, author: str, pages: int):
        super()._init_(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def _str_(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def _repr_(self):
        return f"{self._class.name_}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Аудиокнига."""

    def _init_(self, name: str, author: str, duration: float):
        super()._init_(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def _str_(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность: {self.duration} часов"

    def _repr_(self):
        return f"{self._class.name_}(name={self.name!r}, author={self.author!r}, duration={self.duration})"