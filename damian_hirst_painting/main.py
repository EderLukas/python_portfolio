from turtle import *
# import colorgram
from random import choice


def draw_dot(turtle):
    turtle.pendown()
    turtle.dot(20)
    turtle.penup()
    turtle.fd(50)


def random_color(turtle, color_list):
    new_color = choice(color_list)
    turtle.color(new_color)


def main():
    # color_objects = colorgram.extract("picture/image.jpg", 30)
    #
    # colors = []
    # for obj in color_objects:
    #     r = obj.rgb.r
    #     g = obj.rgb.g
    #     b = obj.rgb.b
    #     colors.append((r, g, b))
    #
    # print(colors)

    color_list = [(241, 246, 243), (131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88),
                  (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71),
                  (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56),
                  (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188),
                  (33, 150, 210), (65, 66, 56)]

    turtle = Turtle()
    screen = Screen()

    # draw 10 by 10 field, dots 20 diameter, pacing between 50
    screen.colormode(255)
    turtle.hideturtle()
    turtle.speed("fastest")

    for i in range(10):
        trtl_y_pos = turtle.ycor()
        turtle.penup()
        turtle.setposition(0, trtl_y_pos + 50)
        turtle.pendown()
        for y in range(10):
            random_color(turtle, color_list)
            draw_dot(turtle)

    screen.exitonclick()


if __name__ == '__main__':
    main()
