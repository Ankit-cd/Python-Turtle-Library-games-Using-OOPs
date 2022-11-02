from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.timmy_body_parts = []
        self.x=0
        self.y=0
        self.create_snake()
        self.head = self.timmy_body_parts[0]
        self.move()

    def create_snake(self):
        for position in positions:
            self.add_segment(position)


    def add_segment(self,position):
        timmy_body = Turtle("square")
        timmy_body.color("white")
        timmy_body.penup()
        timmy_body.goto(position)
        self.timmy_body_parts.append(timmy_body)

    def reset(self):
        for body in self.timmy_body_parts:
            body.goto(1000,1000)
        self.timmy_body_parts.clear()
        self.create_snake()
        self.head=self.timmy_body_parts[0]

    def extend(self):
        self.add_segment(self.timmy_body_parts[-1].pos())

    def move(self):
        for parts in range(len(self.timmy_body_parts) - 1, 0, -1):
            new_x = self.timmy_body_parts[parts - 1].xcor()
            new_y = self.timmy_body_parts[parts - 1].ycor()
            self.timmy_body_parts[parts].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
