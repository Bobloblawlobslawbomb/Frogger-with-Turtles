from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []

    def add_car(self):
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=randint(2, 3))
        new_car.penup()
        new_car.goto(295, randint(-250, 250))
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)