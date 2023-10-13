class Shape:
    def __init__(self, x=float, y=float):
           self.x = x
           self.y = y


    def translate(self, dx, dy):
        try:
            self.x += dx
            self.y += dy
        except TypeError as e:
            raise ValueError("Translation values must be numbers") from e

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y})"


if __name__ == "__main__":
    print("main is working as intended")