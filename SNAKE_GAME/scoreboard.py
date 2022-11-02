from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f"score:{self.score}  High Score:{self.highscore}", align="center",
                   font=("caliber", 16, "italic bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"score:{self.score}  High Score:{self.highscore}", align="center",
                   font=("caliber", 16, "italic bold"))

    # def game_over(self):
    # self.goto(0, 0)
    # self.write("GAME OVER", align="center", font=("caliber", 40, "bold"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highscore}")
        self.clear()
        self.write(f"score:{self.score}  High Score:{self.highscore}", align="center",
                   font=("caliber", 16, "italic bold"))
