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
        self.high_score = 0

    def increase_score(self):
        self.score += 1

    def update_display(self):
        self.undo()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_display()
