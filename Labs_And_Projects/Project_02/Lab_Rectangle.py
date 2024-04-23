import turtle


import math

from Lab_SuperShape import Shape

class Rectangle(Shape):
    def __init__(self, x=float, y=float, side1=float, side2=float):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return (self.side1 + self.side2) * 2

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

    def is_rectangle(self):
        return self.side1 > self.side2 or self.side1 < self.side2

    def is_inside(self, px, py):
        return (
            self.x - self.side1 / 2 <= px <= self.x + self.side1 / 2
            and self.y - self.side2 / 2 <= py <= self.y + self.side2 / 2
        )
    

if __name__ == "__main__":
    print("main is working as intended")