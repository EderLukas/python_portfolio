import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

loop_count = 0
game_is_on = True
while game_is_on:

    # generate cars
    if loop_count % 6 == 0:
        car_manager.create_car()

    # move cars
    car_manager.move()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            loop_count = 0
            scoreboard.game_over_screen()
            
    # is player at finish line
    if player.check_finish():
        player.reset_player()
        loop_count = 0

        car_manager.increase_speed()

        scoreboard.increase_level()
        scoreboard.update_scoreboard()

    # Delete cars that are not on the screen anymore
    for car in car_manager.all_cars:
        if car.xcor() < - 300:
            del car

    # rendering
    time.sleep(0.1)
    screen.update()
    loop_count += 1

screen.exitonclick()
