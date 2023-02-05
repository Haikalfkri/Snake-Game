from turtle import Turtle
import random

class Food(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.random_move()
        
        
    def random_move(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)