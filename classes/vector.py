from math import sqrt


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def Magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def Args(self):
        return self.x, self.y

    def dot(self, other):
        return self.x * other.x + self.y - other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return self.__class__(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return self.__class__(x, y)

    def __mul__(self, scale):
        x = self.x * scale
        y = self.y * scale
        return self.__class__(x, y)

    def __rmul__(self, scale):
        return self * scale

    def __str__(self):
        return f"(x={self.x}, y={self.y})"
