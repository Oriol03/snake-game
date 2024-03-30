from turtle import Turtle
FONT=("Couriel",20,"bold")
class ScoreBoard(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(-60,270)
        
        
    def show_score(self):
        self.clear()
        self.write(arg=f"Score :{self.score}",font=FONT)
        
    def game_over(self):
        self.goto(-60,0)
        self.write(arg="Game Over",font=FONT)