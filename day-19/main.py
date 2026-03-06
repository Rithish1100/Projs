from turtle import Screen,Turtle
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,0,30,60,90]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    game_on=True
    while(game_on):
        for turtle in all_turtle:
            if turtle.xcor()>230:
                game_on=False
                winning_color=turtle.pencolor()
                if winning_color==user_bet:
                    print(f"you have won,Turtle {winning_color} is the winner")
                else:
                    print(f"you have lost, Turtle {winning_color} is the winner")
            
            turtle.forward(random.randint(0,6))

try: 
    screen.exitonclick()
except KeyboardInterrupt:
    pass
screen.mainloop()