import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
screen.register_shape("smallcar2.gif")

turtle.colormode(255)
color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
              (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
              (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217),
              (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0),
              (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]
turtle = Turtle()
turtle.hideturtle()


class Car():
    def __init__(self):
        self.X = 280
        self.Y = 0
        self.turtle_cars = []
        self.create_car()

    def add_car(self):
        timmy = Turtle("smallcar2.gif")
        timmy.shapesize(stretch_wid=1, stretch_len=3)
        timmy.color(random.choice(color_list))
        timmy.penup()
        timmy.goto(self.X, self.Y)
        self.Y = random.randint(-240, 270)
        self.turtle_cars.append(timmy)


    def create_car(self):
        for _ in range(random.randint(0, 1)):
            self.add_car()

    def move_forward(self):
        for turtle in self.turtle_cars:
            turtle.speed("slowest")
            turtle.backward(random.randint(10, 30))

    def game_over(self):
        turtle.color("yellow")
        turtle.goto(0, 0)
        turtle.write("GAME OVER", align="center", font=("caliber", 20, "bold"))
