from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard() 


# Snake Control
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


run = True
while run:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.random_move()
        snake.extend()
        score.increase_score()
        
    
    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        run = False
        score.game_over()
        
    
    # Collision with body
    for seg_index in snake.segments[1:]:
        if snake.head.distance(seg_index) < 10:
            run = False
            score.game_over()

screen.exitonclick()