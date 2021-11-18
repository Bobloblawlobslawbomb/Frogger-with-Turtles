import time
from turtle import Screen, speed
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("TURTLER (frogger w/ a turtle)")
screen.tracer(0)

game_on = True

player = Player()
scoreboard = Scoreboard()
traffic = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

while game_on:
    time.sleep(traffic.speed)
    screen.update()
    traffic.add_car()
    traffic.move_cars()

    if player.ycor() == 280:
        player.go_home()
        scoreboard.level_up()
        traffic.speed_up()

    for car in traffic.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
