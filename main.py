import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")
level = Scoreboard()

cars = CarManager()

car_speed = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()

    # Update car speed
    for car in cars.car_list:
        car.forward(car_speed)
    cars.move_cars()

    # Detect collision of cars with the Turtle
    for car in cars.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    # Detect when turtle arrives at the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_speed += 5
        level.level_up()

screen.exitonclick()
