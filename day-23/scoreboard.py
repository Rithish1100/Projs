from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score=1
    
    def finish(self):
        self.score+=1

    def update_scoreboard(self):
        self.clear()
        self.goto(-240,260)
        self.write(f"LVL:{self.score}",align="center",font=FONT)

    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)
