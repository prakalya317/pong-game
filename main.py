from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("PONG")
my_screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(key="Up", fun=r_paddle.go_up)
my_screen.onkey(key="Down", fun=r_paddle.go_down)
my_screen.onkey(key="w", fun=l_paddle.go_up)
my_screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_paddle misses the ball
    if ball.distance(r_paddle) > 50 and ball.xcor() > 390:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect if l_paddle misses the ball
    if ball.distance(l_paddle) > 50 and ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_r_score()

my_screen.exitonclick()
