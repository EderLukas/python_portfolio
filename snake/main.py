from turtle import Screen, Turtle
import time
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake
snake = Snake()

# listen for inputs
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Game Loop
game_is_on = True
while game_is_on:
    # draw screen
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
