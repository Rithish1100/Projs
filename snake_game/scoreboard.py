from turtle import Turtle
ALIGNMENT="center"
FONT=("couier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r")as data:
            self.high_score =int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=265)
        self.color("white")
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.write(arg=f"Score:{self.score}High score:{self.high_score}",move=False,align=ALIGNMENT,font=FONT)

    def incriment(self):
        self.clear()
        self.score+=1
        self.updatescoreboard()
    
    def reset(self):
        self.clear()
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w")as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.updatescoreboard()

    