from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Generate all the cars and move them in the screen
class Car(Turtle):
    """Cars moving in the -x direction, starting at a random y coordinate"""

    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape('square')
        self.penup()
        self.color(choice(COLORS))
        self.setposition(x=280, y=randint(-280, 280))
        self.car_speed = STARTING_MOVE_DISTANCE


class CarManager:

    def __init__(self):
        self.car_list = []

    def add_car(self):
        """Adds a specified number of cars to the list. Uses randomness to control the generation of cars"""
        if randint(1, 6) == 1:
            car = Car()
            self.car_list.append(car)

    def move_cars(self):
        """Moves all cars in a list of cars"""
        for car in self.car_list:
            car.forward(car.car_speed)

