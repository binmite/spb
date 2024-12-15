import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not author:
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_long_book(self) -> bool:
        ...

    def read_page(self, page_number: int) -> str:
        """
        Возвращает содержимое страницы книги.

        :param page_number: Номер страницы для чтения
        :return: Текст страницы

        :raise ValueError: Если номер страницы выходит за пределы книги

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_page(10)  # Возвращает текст 10-й страницы
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page_number < 1 or page_number > self.pages:
            raise ValueError("Номер страницы должен быть в пределах книги")
        ...

    def get_summary(self) -> str:
        ...


if __name__ == "__main__":
    doctest.testmod()

class Car:
    def __init__(self, brand: str, model: str, max_speed: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param max_speed: Максимальная скорость автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 220)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not model:
            raise ValueError("Модель автомобиля не может быть пустой")
        self.model = model

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть целым числом")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed

    def start_engine(self) -> None:
        ...

    def accelerate(self, speed: int) -> None:
        ...

    def get_info(self) -> str:
        ...


if __name__ == "__main__":
    doctest.testmod()

class Table:
    def __init__(self, material: str, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола (например, "дерево", "металл", "стекло")
        :param width: Ширина стола в метрах
        :param height: Высота стола в метрах

        Примеры:
        >>> table = Table("дерево", 1.5, 0.8)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть строкой")
        if not material:
            raise ValueError("Материал стола не может быть пустым")
        self.material = material

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть числом")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть числом")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = height

    def is_stable(self) -> bool:
        ...

    def place_item(self, item: str) -> None:
        ...

    def get_dimensions(self) -> str:

        ...


if __name__ == "__main__":
    doctest.testmod()