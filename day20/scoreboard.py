from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.speed("fastest")

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))
