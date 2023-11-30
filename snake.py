from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
screen = Screen()


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            screen.tracer(0)
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.segments.append(snake)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
       for number in range(len(self.segments)-1, 0, -1):
          new_x = self.segments[number-1].xcor()
          new_y = self.segments[number-1].ycor()
          self.segments[number].goto(x=new_x, y=new_y)

       self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

