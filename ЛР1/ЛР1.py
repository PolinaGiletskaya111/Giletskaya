# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Chocolate_bar:
    def __init__(self, type_chocolate: str, calorific_value: float, chocolate_weight: float):
        """
        Создание и подготовка к работе объекта "Шоколад"
        :param type_chocolate: Тип шоколада (молочный, горький и т.д)
        :param calorific_value: Калорийность в кКл на 100 гр
        :param chocolate_weight: Вес плитки шоколада в граммах

        Примеры:
        >>> chocolate_bar_1 = Chocolate_bar( "Молочный", 100, 150)  # инициализация экземпляра класса
        """
        if not isinstance(type_chocolate, str):
            raise TypeError("Тип шоколада должен быть типа str")
        self.type_chocolate = type_chocolate

        if not isinstance(calorific_value, (int, float)):
            raise TypeError("Калорийность шоколада должен быть типа int или float")
        if calorific_value <= 0:
            raise ValueError("Калорийность шоколада должен быть положительным числом")
        self.calorific_value = calorific_value

        if not isinstance(chocolate_weight, (int, float)):
            raise TypeError("Вес плитки шоколада должен быть типа int или float")
        if chocolate_weight <= 0:
            raise ValueError("Вес плитки шоколада должен быть положительным числом")
        self.chocolate_weight = chocolate_weight

    def diet_chocolate(self) -> bool:
        """
        Функция, которая проверяет, является ли шоколад низкокалорийным
        :return: Является ли шоколад диетическим
        >>> chocolate_bar_1 = Chocolate_bar("Горький", 100, 150)
        >>> chocolate_bar_1.diet_chocolate()
        """
        ...

    def chocolate_fondue(self) -> bool:
        """
        Функция проверяет, подходит ли этот шоколад по рецепту для шоколадного фондана
        :return: Подходит ли шоколад по рецепту
        >>> chocolate_bar_2 = Chocolate_bar("Горький", 100, 150)
        >>> chocolate_bar_2.chocolate_fondue()
        """
        ...


class Vine:
    def __init__(self, type_grape: str, color_vine: str, year: int):
        """
        Создание и подготовка к работе объекта "Вино"
        :param type_grape: Тип винограда
        :param color_vine: Цвет вина
        :param year: Год сбора урожая

        Примеры:
        >>> vine_1 = Vine( "Изабелла", "Красный", 2018)  # инициализация экземпляра класса
        """
        if not isinstance(type_grape, str):
            raise TypeError("Тип винограда должен быть типа str")
        self.type_grape = type_grape

        if not isinstance(color_vine, str):
            raise TypeError("Цвет вина должен быть типа str")
        self.color_vine = color_vine

        if not isinstance(year, int):
            raise TypeError("Год сбора урожая должен быть типа int")
        if year <= 0:
            raise ValueError("Год сбора урожая должен быть положительным числом")
        self.year = year

    def vine_sale(self) -> bool:
        """
        Функция проверяет, подходит ли это вино для продажи
        :return: Подходит ли вино для продажи
        >>> vine_1 = Vine( "Изабелла", "Красный", 2018)
        >>> vine_1.vine_sale()
        """
        ...

    def vine_meat(self) -> bool:
        """
        Функция проверяет, подходит ли это вино для готовки мяса
        :return: Подходит ли вино для гоовки мяса
        >>> vine_2 = Vine( "Изабелла", "Красный", 2018)
        >>> vine_2.vine_meat()
        """
        ...


class Route:
    def __init__(self, point_a: str, point_b: str, route_distance: float):
        """
        Создание и подготовка к работе объекта "Маршрут"
        :param point_a: Пункт отправления А
        :param point_b: Пункт назанчения Б
        :param route_distance: Расстояние между пунктами

        Примеры:
        >>> route_1 = Route( "Санкт-Петерубрг", "Москва", 702)  # инициализация экземпляра класса
        """
        if not isinstance(point_a, str):
            raise TypeError("Пункт отправления А должен быть типа str")
        self.point_a = point_a

        if not isinstance(point_b, str):
            raise TypeError("Пункт назанчения Б должен быть типа str")
        self.point_b = point_b

        if not isinstance(route_distance, (float, int)):
            raise TypeError("Расстояние между пунктами должен быть типа int или float")
        if route_distance <= 0:
            raise ValueError("Расстояние между пунктами должен быть положительным числом")
        self.route_distance = route_distance

    def get_time(self) -> bool:
        """
        Функция проверяет, успеем ли добраться до Пункта Б
        :return: Успеем ли добраться
        >>> route_1 = Route( "Санкт-Петерубрг", "Москва", 702)
        >>> route_1.get_time()
        """
        ...

    def fuel(self) -> bool:
        """
        Функция проверяет, хватит ли нам топлива
        :return: Хватит ли топлива
        >>> route_2 = Route( "Санкт-Петерубрг", "Москва", 702)
        >>> route_2.fuel()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
