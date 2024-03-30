from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("magenta")
        self.random_place()
        
    def random_place(self):
        self.clear()
        new_x=random.randint(-270,270)
        new_y=random.randint(-270,270)
        self.goto(new_x,new_y)
        

