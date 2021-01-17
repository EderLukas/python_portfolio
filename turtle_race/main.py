from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtel will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_pos = -100

for i in range(6):
    turtles.append(Turtle("turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=y_pos)
    y_pos += 25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.fd(random.randint(1, 10))

screen.exitonclick()
