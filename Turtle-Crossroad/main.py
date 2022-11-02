from turtle import Screen
from ourturtle import Move
from car import Car
from level import Level
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY TURTLE CROSSROAD")
my_turtle = Move()
car = Car()
level = Level()
screen.listen()

screen.onkey(my_turtle.move_forward, "Up")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(level.movement_speed)
    car.move_forward()
    car.create_car()
    if my_turtle.ycor() > 280:
        level.increase()
        my_turtle.refresh()
    for cars in car.turtle_cars:
        if my_turtle.distance(cars) < 25:
            game_is_on = False
            car.game_over()

screen.exitonclick()
