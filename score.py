from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")

class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.penup()
        self.goto(0, 250)
        self.color("black")
        self.write(f"Score: 0", align=ALIGNMENT,font=FONT)
        self.hideturtle()
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 80, "bold"))
