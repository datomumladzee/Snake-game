from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.color("yellow")
        self.write(f"💀 GAME OVER 💀 ", align="center", font=("Arial", 22, "normal"))

    def update_score(self):
        self.clear()

    def increase_score(self):
        self.score += 1
        self.write(f"Score:{self.score}", align="center", font=("Arial", 15, "normal"))

