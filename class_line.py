import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x)**2 +
                        (self.end.y - self.start.y)**2)

    def compute_slope(self):
        dx = (self.end.x - self.start.x)
        dy = (self.end.y - self.start.y)
        if dx == 0:
            return 90  # vertical line
        angle = math.degrees(math.atan(dy/dx))
        return angle

    def compute_horizontal_cross(self):
        return (self.start.y == 0 or self.end.y == 0 or
                (self.start.y < 0 < self.end.y) or
                (self.end.y < 0 < self.start.y))

    def compute_vertical_cross(self):
        return (self.start.x == 0 or self.end.x == 0 or
                (self.start.x < 0 < self.end.x) or
                (self.end.x < 0 < self.start.x))

class Rectangle:
    def __init__(self, line1, line2, line3, line4):
        self.lines = [line1, line2, line3, line4]

    def compute_perimeter(self):
        return sum(line.length for line in self.lines)

    def compute_area(self):
        side1 = self.lines[0].length
        side2 = self.lines[1].length
        return side1 * side2

# Line
p1 = Point(0, 0)
p2 = Point(3, 4)

line = Line(p1, p2)

print("Length:", line.length)
print("Slope:", line.slope)
print("intersection with x-axis?", line.compute_horizontal_cross())
print("intersection with y-axis?", line.compute_vertical_cross())

# Horizontal/Vertical lines
h = Line(Point(0, 2), Point(5, 2))
v = Line(Point(3, -1), Point(3, 4))

print(h.slope)
print(v.slope)

# Rectangle
A = Point(0, 0)
B = Point(4, 0)
C = Point(4, 3)
D = Point(0, 3)

l1 = Line(A, B)
l2 = Line(B, C)
l3 = Line(C, D)
l4 = Line(D, A)

rect = Rectangle(l1, l2, l3, l4)

print("Perimeter:", rect.compute_perimeter())
print("Area:", rect.compute_area())
