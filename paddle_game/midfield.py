from turtle import Turtle


class Midfield(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.setheading(270)
        self.backward(300)

        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
