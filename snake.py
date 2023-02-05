from turtle import Turtle

POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.snake_position()
        self.head = self.segments[0]
        
    
    def snake_position(self):    
        for pos in POSITION:
            self.create_snake(pos)
            
        
    def create_snake(self, position):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
        
     
    def extend(self):
        self.create_snake(self.segments[-1].position())   
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
        
        
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    
        