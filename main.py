from turtle import Screen, Turtle
from paddle1 import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_SIZE_LEN = (800)
SCREEN_SIZE_WIDTH = (600)
WINNING_SCORE = 10

screen = Screen()
screen.setup(SCREEN_SIZE_LEN,SCREEN_SIZE_WIDTH)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "e")
screen.onkey(paddle2.down, "d")

ball = Ball()
scoreboard = Scoreboard()
winner = Turtle()

game_is_on = True


time.sleep(1)
while game_is_on:
    time.sleep(0)
    screen.update()
    ball.move()

    #detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detect if paddle1 misses
    if ball.xcor() >380 :
        time.sleep(1)
        ball.reset_position()
        scoreboard.increase_score_l()

    # detect if paddle1 misses
    if ball.xcor() < -380 :
        time.sleep(1)
        ball.reset_position()
        scoreboard.increase_score_r()


    if scoreboard.r_score >= WINNING_SCORE or scoreboard.l_score >= WINNING_SCORE:
        winner.penup()
        ball.hideturtle()
        if scoreboard.l_score > scoreboard.r_score:
            winner.penup()
            winner.hideturtle()
            winner.color("white")
            winner.goto(0, 0)
            winner.write("LEFT SIDE WON", align="center", font=("Courier", 80, "normal"))

        else:
            winner.penup()
            winner.hideturtle()
            winner.color("white")
            winner.goto(0, 0)
            winner.write("RIGHT SIDE WON", align="center", font=("Courier", 80, "normal"))
        game_is_on = False



screen.update()
screen.exitonclick()
