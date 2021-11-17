import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("TURTLER (frogger w/ a turtle)")
screen.tracer(0)

game_is_on = True

player = Player()
scoreboard = Scoreboard()

traffic = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in traffic.car_list:
        traffic.car_move()

    if player.ycor() == 280:
        print("You win!")
        player.go_home()
        scoreboard.level_up()


# move car(s) across the screen


# detect collision between player and cars --use distance()
