from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
PADDING = 40


class Score(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=screen_height / 2 - PADDING)
        self.score = 0
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
