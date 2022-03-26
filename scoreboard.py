from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
PADDING = 40


class Score(Turtle):

    def __init__(self, max_y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=max_y - PADDING)
        self.score = 0
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.setposition(0,0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
