import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_display()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 \
            or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
