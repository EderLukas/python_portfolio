from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def change_y_direction(self):
        self.y_movement *= -1

    def change_x_direction(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.change_x_direction()
        self.move_speed = 0.1
