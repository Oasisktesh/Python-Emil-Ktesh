from Lab_SuperShape import Shape


import math

class Circle(Shape):
    def __init__(self, x=float, y=float, radius=float):
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_equal(self, other):
        return self.area == other.area

    def is_less(self, other):
        return self.area < other.area

    def is_more(self, other):
        return self.area > other.area

    def is_less_or_equal(self, other):
        return self.area <= other.area

    def is_more_or_equal(self, other):
        return self.area >= other.area

    def is_unit_circle(self):
        return self.radius == 1

    def is_inside(self, px, py):
        distance = math.sqrt((self.x - px) ** 2 + (self.y - py) ** 2)
        return distance <= self.radius

if __name__ == "__main__":
    print("main is working as intended")