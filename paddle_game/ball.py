from turtle import Turtle

import random


INITIAL_DIST = [10, -10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0
        self.y_move = 0
        self.rand_dir()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self, color):
        self.x_move *= -1

        self.move_speed *= 0.80

        self.color(color)

    def reset_position(self):
        self.goto(0, 0)
        self.color("white")
        self.move_speed = 0.1
        self.rand_dir()

    def rand_dir(self):
        self.x_move = random.choice(INITIAL_DIST)
        self.y_move = random.choice(INITIAL_DIST)


