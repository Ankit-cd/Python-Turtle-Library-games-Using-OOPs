from turtle import Turtle


class Move(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -275)

    def move_forward(self):
        self.speed("fastest")
        self.forward(10)

    def refresh(self):
        self.setheading(90)
        self.penup()
        self.goto(0, -275)
