class Animal:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class Zebra(Animal):

    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def __str__(self):
        return " ".join(["Имя:", self.get_name(), "\n",
                         "Возраст:", self.get_age(), "\n",
                         "Цвет:", self.get_colour(), "\n"])


class Dolphin(Animal):

    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return " ".join(["Имя:", self.get_name(), "\n",
                         "Возраст:", self.get_age(), "\n",
                         "Вес:", self.get_weight(), "\n"])


a = Zebra("Шарик", "1 год", "черно-белый")
print(a)
b = Dolphin("Бобик", "2 года", "100 кг")
print(b)
