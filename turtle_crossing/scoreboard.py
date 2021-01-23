from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over_screen(self):
        self.goto(0, 0)
        self.write(arg="Game over!", align="center", font=FONT)
