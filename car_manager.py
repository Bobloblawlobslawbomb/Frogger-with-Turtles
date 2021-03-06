from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

CAR_SPEED = 0.1
CAR_SPEED_MULTIPLIER = 0.9


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.speed = CAR_SPEED

    def add_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=randint(2, 3))
            new_car.penup()
            new_car.goto(295, randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.speed *= CAR_SPEED_MULTIPLIER
