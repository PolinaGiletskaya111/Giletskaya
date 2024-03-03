if __name__ == "__main__":
    # Write your solution here
    pass
class Deciduous_trees:
    """ Базовый класс лиственные деревья"""
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Дерево {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"

    def type_tree(self) -> bool:
        """
        Функция, которая проверяет, относитя ли дерево к лиственным
        :return: Является ли дерево лиственным
        >>> maple = Deciduous_trees("Клён")
        >>> maple.type_tree()
        """
        ...

    def life_tree(self) -> bool:
        """
        Функция, которая определяет, относитя ли порода дерева к "долгожителям" (Продолжительность жизни более 300 лет)
        :return: Является ли парода дерева "долгожителем"
        >>> maple = Deciduous_trees("Клён")
        >>> maple.life_tree()
        """
        ...


class Oak(Deciduous_trees):
    def __init__(self, name, life_time: int, float):
        super().__init__(name)
        if not isinstance(life_time, (int, float)):
            raise TypeError("Продолжительность жизни должна быть типа int или float")
        if life_time <= 0:
            raise ValueError("Продолжительность жизни должна быть положительным числом")
        self.life_time = life_time

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, life_time={self.life_time!r})"

    def __str__(self):
        return f"Дерево {self.name}. Продолжительность жизни {self.life_time}"

    def life_tree(self) -> bool:
        """
        Функция, которая проверяет заданную продолжительность жизни, сравнивает её с исходной среднестатистической
        и определяет, относитя ли дерево к "долгожителям" (Продолжительность жизни более 300 лет)
        :return: Является ли дерево "долгожителем"
        >>> Oak_1 = Deciduous_trees("Дуб", 400)
        >>> Oak_1.life_tree()
        """
        ...


class Birch(Deciduous_trees):
    def __init__(self, name, location: str):
        super().__init__(name)
        if not isinstance(location, str):
            raise TypeError("Местоположение должно быть типа str")
        self.location = location

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, location={self.location!r})"

    def __str__(self):
        return f"Дерево {self.name}. Местоположение {self.location}"