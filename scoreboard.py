from turtle import Turtle
import time
import random

ALIGN = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self, level_name=""):
        super().__init__()
        self.score = 0
        self.level_name = level_name
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

        # Display level below score
        self.goto(0, 230)
        self.write(f"Level: {self.level_name}", align=ALIGN, font=("Courier", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.color(random.choice(["white", "cyan", "magenta", "lime"]))
        self.update()

    def game_over(self):
        self.goto(0, 0)
        for _ in range(3):
            self.clear()
            self.write("GAME OVER", align=ALIGN, font=("Courier", 28, "bold"))
            time.sleep(0.3)
            self.clear()
            time.sleep(0.2)
        self.write("GAME OVER\nPress R to Restart", align=ALIGN, font=("Courier", 20, "bold"))
