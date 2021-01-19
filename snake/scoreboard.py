from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def update_display(self):
        self.undo()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
