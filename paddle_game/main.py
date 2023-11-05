from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from midfield import Midfield
import time

X_LIMIT = 380

# paddle colors
r_color = "green"
l_color = "red"

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paddles setup
right_paddle = Paddle((350, 50))
left_paddle = Paddle((-350, 50))
right_paddle.color(r_color)
left_paddle.color(l_color)

# other objects
ball = Ball()
scoreboard = Scoreboard()
midfield = Midfield()

screen.update()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # paddle hits
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.setx(320)
        ball.hit(r_color)

    elif ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.setx(-320)
        ball.hit(l_color)

    # scoreboard recorder
    if ball.xcor() > X_LIMIT or ball.xcor() < -X_LIMIT:
        scoreboard.add_score(ball.xcor())
        ball.reset_position()
        right_paddle.reset_pos(350)
        left_paddle.reset_pos(-350)
        time.sleep(1.5)

    if scoreboard.winner != "":
        game_on = False

screen.exitonclick()
