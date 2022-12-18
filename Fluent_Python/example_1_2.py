import math


class Vector:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    a_vec = Vector(1, 1)
    b_vec = Vector(2, 2)

    print(bool(a_vec))
