import turtle
import random


def draw_line(p1, p2):
    pass



size = 20
points = [(random.randint(100, 1180), random.randint(100, 980)) for i in range(size)]
n = 1
while(1) :
    draw_line(points[n-1],points[n])
    n = (n + 1) % size


turtle.done()