from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        # self.create_traffic()
        self.add_car()
        self.add_car()
        self.add_car()

    # def create_traffic(self):
    #     for color in COLORS:
    #         self.add_car(color)

    def add_car(self):
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=randint(2, 3))
        new_car.penup()
        new_car.goto(295, randint(-250, 250))
        self.car_list.append(new_car)

    def car_move(self):
        x_cor = self.xcor() + MOVE_INCREMENT
        self.goto(x_cor, self.ycor())
