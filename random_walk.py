from turtle import Turtle, Screen
import random

walker = Turtle()
walker.pensize(10)
walker.speed(0)
direction = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)


def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    gen_color = (r, g, b)
    return gen_color


for i in range(1000):
    num = random.randint(1, 2)
    tur_color = color_generator()
    walker.pencolor(tur_color)
    walker.setheading(random.choice(direction))
    walker.forward(20)

screen.exitonclick()
