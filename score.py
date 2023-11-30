from turtle import Turtle
from snake import Snake


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-40, 260)
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 35, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
