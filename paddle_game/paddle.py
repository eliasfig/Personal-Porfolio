from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=0.5)
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def reset_pos(self,xcor):
        if xcor > 0:
            self.goto(350, 0)
        else:
            self.goto(-350,0)
