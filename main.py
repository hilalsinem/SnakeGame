from turtle import Turtle, Screen
from snake import Snake
from score import Score
import time
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
my_food = Food()

my_score = Score()
my_snake = Snake()
is_game_on = True
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")
screen.onkey(my_snake.left, "Left")

while is_game_on:
    screen.update()

    time.sleep(0.09)
    my_snake.move()
    if my_snake.head.distance(my_food) < 20:
        my_score.update_score()
        my_snake.extend()
        my_food.refresh()
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        my_score.game_over()
        is_game_on = False
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            my_score.game_over()
            is_game_on = False


screen.exitonclick()
