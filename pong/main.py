import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Setup main screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for opponent_paddle key inputs
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

# game loop / game logic
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)

    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y_direction()

    # Paddle bounce
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or\
            (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.change_x_direction()

    # Point / Reset ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # move ball
    ball.move()

    # update drawing
    screen.update()


screen.exitonclick()

