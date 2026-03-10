from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scoreboard=Scoreboard()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.mov()

    #Detect with wall
    if ball.ycor()> 280 or ball.ycor()< -280:
        ball.bounce_y()

    #Detect with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.ycor()>-325:
        ball.bounce_x()

    #Detect if ball moves out of bound
    if ball.xcor()>390:
        scoreboard.lpoint()
        ball.reset_pos()
    
    if ball.xcor()<-390:
        scoreboard.rpoint()
        ball.reset_pos()

screen.exitonclick()