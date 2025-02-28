from abc import ABC, abstractmethod

class Appliance(ABC):
    """
    Абстрактный класс, представляющий бытовой прибор.

    Атрибуты:
    - brand (str): Бренд прибора.
    - power (int): Мощность в ваттах.
    """

    def __init__(self, brand: str, power: int):
        if power <= 0:
            raise ValueError("Мощность должна быть положительной.")
        self.brand = brand
        self.power = power

    @abstractmethod
    def turn_on(self) -> str:
        """
        Метод, который включает прибор.

        :return: Сообщение о включении прибора.
        :rtype: str
        :doctest:
        >>> fridge = Refrigerator("Samsung", 150)
        >>> fridge.turn_on()
        'Refrigerator is now on.'
        """
        ...

class Refrigerator(Appliance):
    def turn_on(self) -> str:
        return "Refrigerator is now on."

class Book(ABC):
    """
    Абстрактный класс, представляющий книгу.

    Атрибуты:
    - title (str): Название книги.
    - author (str): Автор книги.
    - pages (int): Количество страниц.
    """

    def __init__(self, title: str, author: str, pages: int):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> str:
        """
        Метод, который возвращает сообщение о чтении книги.

        :return: Сообщение о чтении.
        :rtype: str
        :doctest:
        >>> novel = Novel("1984", "George Orwell", 328)
        >>> novel.read()
        'Reading 1984 by George Orwell.'
        """
        ...

class Novel(Book):
    def read(self) -> str:
        return f"Reading {self.title} by {self.author}."

class Gadget(ABC):
    """
    Абстрактный класс, представляющий гаджет.

    Атрибуты:
    - name (str): Название гаджета.
    - version (str): Версия гаджета.
    """

    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    @abstractmethod
    def update(self) -> str:
        """
        Метод, который обновляет гаджет.

        :return: Сообщение об обновлении.
        :rtype: str
        :doctest:
        >>> phone = Smartphone("iPhone", "14.0")
        >>> phone.update()
        'Updating iPhone to version 14.1.'
        """
        ...

class Smartphone(Gadget):
    def update(self) -> str:
        new_version = "14.1"  # Пример новой версии
        return f"Updating {self.name} to version {new_version}."
