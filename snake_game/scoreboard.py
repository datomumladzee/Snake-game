from tkinter.constants import SEL_LAST
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()