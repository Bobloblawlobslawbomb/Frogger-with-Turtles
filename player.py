from turtle import Turtle
from random import randint

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.go_home()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def left(self):
        x_pos = self.xcor() - MOVE_DISTANCE
        self.setpos(x_pos, self.ycor())

    def right(self):
        x_pos = self.xcor() + MOVE_DISTANCE
        self.setpos(x_pos, self.ycor())

    def go_home(self):
        self.goto(randint(-100, 100), -280)
