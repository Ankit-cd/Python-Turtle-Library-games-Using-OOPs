from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 1
        self.movement_speed = 0.8
        self.penup()
        self.goto(-250, 270)
        self.color("white")
        self.write(f"Level:{self.number}", align="center", font=("caliber", 16, "italic"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.number += 1
        self.movement_speed *= 0.9
        self.write(f"Level:{self.number}", align="center", font=("caliber", 16, "italic"))
