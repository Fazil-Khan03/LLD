from abc import ABC, abstractmethod

class Shapes(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shapes):

    def draw(self):
        print("Drawing the circle!")

class Square(Shapes):

    def draw(self):
        print("Drawing the Square")

class Rectangle(Shapes):

    def draw(self):
        print("Drawing the Rectangle")

class ShapeFactory:

    @staticmethod
    def get_shapes(type):
        if type == 'Circle':
            return Circle()
        elif type == 'Square':
            return Square() 
        elif type == 'Rectangle':
            return Rectangle()

choice = 'Square'
shape = ShapeFactory().get_shapes(choice)
shape.draw()

choice = 'Rectangle'
shape = ShapeFactory().get_shapes(choice)
shape.draw()

