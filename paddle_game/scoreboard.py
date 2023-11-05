from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
Y_COR = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, Y_COR)
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.winner = ""
        self.write(f"{self.left_score}   {self.right_score}", align=ALIGNMENT, font=FONT)

    def add_score(self, x_cor):
        if x_cor > 0:
            self.left_score += 1
        else:
            self.right_score += 1

        self.clear()
        self.write(f"{self.left_score}   {self.right_score}", align=ALIGNMENT, font=FONT)
        self.check_winner()

    def check_winner(self):

        if self.left_score == 7 or self.right_score == 7:
            self.goto(0, 0)
            self.winner = " "
            self.write(f"We have    a winner!", align=ALIGNMENT, font=FONT)


