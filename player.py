from turtle import Turtle

FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def up(self):
        self.seth(90)
        self.forward(10)

    def down(self):
        if self.ycor() >= -251:
            self.seth(270)
            self.forward(10)

    def reset_pos(self):
        self.goto(0, -250)

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False