from turtle import Turtle, Screen


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clear_screen():
    tim.home()
    tim.clear()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
