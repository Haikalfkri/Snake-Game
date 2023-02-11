from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:/Documents/Haikal\Python/day 24 files, directory and paths/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("D:/Documents/Haikal\Python/day 24 files, directory and paths/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0


        self.update_scoreboard()

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()