# Purpose: create a class circle for each individual circle in the bullseye
from cs1lib import *

class Circle:
    def __init__(self, gx, gy, radius, r, g, b):
        self.x = gx
        self.y = gy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    # moving the circle by a velocity, will call in Bullseye class
    def update(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy

    def draw(self):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)

    def __str__(self):
        return str(self.x) + " " + str(self.y)
