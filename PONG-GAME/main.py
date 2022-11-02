from turtle import Screen
from mainscreen import MainScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("MY PONG GAME")

body = MainScreen()
paddle = Paddle(x=350, y=0)

paddle2 = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "q")
screen.onkey(paddle2.down, "z")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collisions with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # detect collisions with the paddle
    if ball.distance(paddle)<50 and ball.xcor()>325 or ball.distance(paddle2)<50 and ball.xcor()<-325:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
