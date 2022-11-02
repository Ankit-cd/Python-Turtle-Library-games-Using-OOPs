from turtle import Turtle


class MainScreen:
    def __init__(self):
        self.x = 0
        self.y = 280
        self.create_body()

    def create_body(self):
        for a in range(0, 29):
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            timmy.shapesize(stretch_len=0.5, stretch_wid=0.2)
            timmy.setheading(270)
            timmy.goto(self.x, self.y)
            self.y -= 20
