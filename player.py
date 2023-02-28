from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# The Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > 290:
            return True
        else:
            return False

    def go_to_start(self):
        self.setposition(STARTING_POSITION)
