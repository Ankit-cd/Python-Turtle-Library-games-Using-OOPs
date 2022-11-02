from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.X = x
        self.Y = y
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.X, self.Y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
