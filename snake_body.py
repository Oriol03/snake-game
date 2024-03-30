from turtle import Turtle
START_POSITION=[(0,0),(-20,0),(-40,0)]
class Snake :
    
    def __init__(self) :
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    def create_snake(self):
        for  position in START_POSITION:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1) :
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(20)
    
    def extend(self):
        last_segment_position=self.segments[-1].position()
        self.add_segment(last_segment_position)   
    
    
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270) 