class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1=None, p2=None, center=None, width=None, height=None):
        # Method 1: Bottom-left corner(Point) + width and height
        if p1 and width and height:
            self.width = width
            self.height = height
            self.center = Point(p1.x + width/2, p1.y + height/2)

        # Method 2: Center(Point) + width and height
        elif center and width and height:
            self.width = width
            self.height = height
            self.center = center

        # Method 3: Two opposite corners (Points)
        elif p1 and p2:
            self.width = abs(p2.x - p1.x)
            self.height = abs(p2.y - p1.y)
            self.center = Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_interference_point(self, p):
        left   = self.center.x - self.width/2
        right  = self.center.x + self.width/2
        bottom = self.center.y - self.height/2
        top    = self.center.y + self.height/2

        return (left <= p.x <= right) and (bottom <= p.y <= top)


class Square(Rectangle):
    def __init__(self, p1=None, p2=None, center=None, side=None):

        if center and side:
            super().__init__(center=center, width=side, height=side)

        elif p1 and side:
            super().__init__(p1=p1, width=side, height=side)

        elif p1 and p2:
            side = abs(p2.x - p1.x)
            super().__init__(p1=p1, width=side, height=side)

# Rectangle
r1 = Rectangle(p1=Point(0, 0), width=4, height=2)
print("Area:", r1.compute_area())           
print("Perimeter:", r1.compute_perimeter()) 
print("Center:", (r1.center.x, r1.center.y))
p = Point(1, 1)
print("Inside: ", r1.compute_interference_point(p))

# Square
s2 = Square(center=Point(10, 10), side=4)
print("Perimeter:", s2.compute_perimeter())
