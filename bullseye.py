# Purpose: create the Bullseye class which consists of three Circle objects
from circle import Circle

class Bullseye:
    def __init__(self, gx, gy, size, vx, vy):
        self.x = gx
        self.y = gy
        self.size = size
        self.vx = vx
        self.vy = vy
        self.c1 = Circle(gx, gy, size, 1, 0, 0)
        self.c2 = Circle(gx, gy, 2*size, 0, 1, 0)
        self.c3 = Circle(gx, gy, 3*size, 0, 0, 1)

    # move the whole target by calling Circle update method on each circle
    def update(self):
        self.c1.update(self.vx, self.vy)
        self.c2.update(self.vx, self.vy)
        self.c3.update(self.vx, self.vy)

    def draw(self):
        self.c3.draw()
        self.c2.draw()
        self.c1.draw()

    #checks whether mouse is within the target or not (if it is returns true, if it isn't returns false
    def within_bullseye(self, x, y):
        if self.c1.x - self.c1.radius <= x <= self.c1.x + self.c1.radius and self.c1.y - self.c1.radius <= y <= self.c1.y + self.c1.radius:
            return True
        else:
            return False


