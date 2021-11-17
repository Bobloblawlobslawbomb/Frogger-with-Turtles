from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(
            f"Level: {self.level}",
            align="center",
            font=FONT
        )

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.write(
            "GAMEOVER.",
            align="center",
            font=("Courier", 50, "normal")
        )
