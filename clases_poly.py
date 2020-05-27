class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        print(f"x: {self.x} y: {self.y}")
        pass

    def who_am_i(self):
        print(f"I'm a great point at {self.x}, {self.y}")


class Circle(Point):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = 0

    def draw(self):
        print(f"x: {self.x} y: {self.y}, r: {self.radius}")

    def who_am_i(self):
        print(f"I'm a great circle at {self.x}, {self.y} with {self.radius}")


a = Point(1, 2)
b = Circle(2, 3,4)
c = Point(4,6)

d = [a, b, c]
for _ in d:
    _.draw()
