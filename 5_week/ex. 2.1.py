class Shape:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height


class Triangle(Shape):

    def area(self):
        return (1/2)*(self.get_width()*self.get_height())


class Rectangle(Shape):

    def area(self):
        return (self.get_width()*self.get_height())


a = Triangle(10, 12)
a.area()
print(a.area())
a.set_height(20)
print(a.area())
b = Rectangle(10, 12)
b.area()
print(b.area())