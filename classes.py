class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = 'None'

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = 'woof'


if __name__ == '__main__':
    dog = Dog('Dog')
    animal = Animal('Animal')

    print(dog.make_sound())
    print(animal.make_sound())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'{self.x}, {self.y}'


if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    print(point1 + point2)