from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self,intx,inty):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1,stretch_len=3,outline=None)
        self.penup()
        self.goto(x=intx,y=inty)
        a=self.xcor()
        self.inta=0
    
    def move(self,intx):
        new_xcor=(self.xcor()-intx)-self.inta
        self.goto(new_xcor,self.ycor())
    
    def incriment(self):
        self.inta+=MOVE_INCREMENT
    
