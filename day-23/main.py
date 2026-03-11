import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing")

player=Player()
car_manager1=CarManager(280,-260)
car_manager2=CarManager(280,-220)
car_manager3=CarManager(280,-180)
car_manager4=CarManager(280,-140)
car_manager5=CarManager(280,-100)
car_manager6=CarManager(280,-60)
car_manager7=CarManager(280,-20)
car_manager8=CarManager(280,20)
car_manager9=CarManager(280,60)
car_manager10=CarManager(280,100)
car_manager11=CarManager(280,140)
car_manager12=CarManager(280,180)
car_manager13=CarManager(280,220)
car_manager14=CarManager(280,260)

scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    screen.update()
    if car_manager1.xcor()>-320:
        car_manager1.move(6.4)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager1.goto(280,-260)

    if car_manager2.xcor()>-320:
        car_manager2.move(3.4)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager2.goto(280,-220)

    if car_manager3.xcor()>-320:
        car_manager3.move(7.4)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager3.goto(280,-180)

    if car_manager4.xcor()>-320:
        car_manager4.move(2.5)
        time.sleep(0.01)
        screen.update()
    else: 
        car_manager4.goto(280,-140)

    if car_manager5.xcor()>-320:
        car_manager5.move(7.5)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager5.goto(280,-100)

    if car_manager6.xcor()>-320:
        car_manager6.move(4.5)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager6.goto(280,-60)

    if car_manager7.xcor()>-320:
        car_manager7.move(3.5)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager7.goto(280,-20)

    if car_manager8.xcor()>-320:
        car_manager8.move(7.9)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager8.goto(280,20)

    if car_manager9.xcor()>-320:
        car_manager9.move(4.6)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager9.goto(280,60)

    if car_manager10.xcor()>-320:
        car_manager10.move(10)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager10.goto(280,100)

    if car_manager11.xcor()>-320:
        car_manager11.move(2)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager11.goto(280,140)

    if car_manager12.xcor()>-320:
        car_manager12.move(7.4)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager12.goto(280,180)

    if car_manager13.xcor()>-320:
        car_manager13.move(5.9)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager13.goto(280,220)

    if car_manager14.xcor()>-320:
        car_manager14.move(1)
        time.sleep(0.01)
        screen.update()
    else:
        car_manager14.goto(280,260)
    if player.distance(car_manager1)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager2)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager3)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager4)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager5)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager6)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager7)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager8)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager9)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager10)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager11)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager12)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager13)<40:
        scoreboard.game_over()
        game_is_on=False
    if player.distance(car_manager14)<40:
        scoreboard.game_over()
        game_is_on=False

    if player.ycor()>280:
        scoreboard.finish()
        car_manager1.incriment()
        car_manager2.incriment()
        car_manager3.incriment()
        car_manager4.incriment()
        car_manager5.incriment()
        car_manager6.incriment()
        car_manager7.incriment()
        car_manager8.incriment()
        car_manager9.incriment()
        car_manager10.incriment()
        car_manager11.incriment()
        car_manager12.incriment()
        car_manager13.incriment()
        car_manager14.incriment()

        scoreboard.update_scoreboard()
        player.player_reset()
screen.exitonclick()