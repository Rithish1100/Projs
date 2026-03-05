import turtle as t
import random

t.colormode(255)
color_list=[(222, 224, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232)]
tim=t.Turtle()
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dots_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dots_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)

        tim.forward(500)
        tim.setheading(0)


screen=t.Screen()
screen.exitonclick()
#sprograph
'''
tim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return(random_color)
tim.speed("fastest")

def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(size_of_gap)
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

spirograph(5)


screen=t.Screen()
screen.exitonclick()
'''
