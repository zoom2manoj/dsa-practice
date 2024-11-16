from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def __init__(self, color):
        self.color = color
    def clone(self):
        return Circle(self.color)

    def draw(self):
        print(f"This is {self.color} color cirle draw")

class Square(Shape):

    def __init__(self, size):
        self.size = size
    def clone(self):
        return Square(self.size)

    def draw(self):
        print(f"This is {self.size} size square draw")


class Client:
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        self.shape.clone()
        self.shape.draw()
if __name__ == "__main__":
    cirle = Circle("Red")
    square = Square("5")

    client = Client(cirle)
    client.draw()
    client = Client(square)
    client.draw()

