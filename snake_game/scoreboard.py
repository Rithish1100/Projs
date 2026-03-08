from turtle import Turtle
ALIGNMENT="center"
FONT=("couier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=265)
        self.color("white")
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.write(arg=f"Score:{self.score}",move=False,align=ALIGNMENT,font=FONT)

    def incriment(self):
        self.clear()
        self.score+=1
        self.updatescoreboard()
    
    def gameover(self):
        self.goto(x=0,y=0)
        self.write(arg=f"GAME OVER",move=False,align=ALIGNMENT,font=FONT)

    