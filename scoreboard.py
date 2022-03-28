import tarfile
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
        self.high_score = self.get_high_score()
        self.color("white")
        self.write_score()

    def get_high_score(self):
        try:
            with open("high_score.txt") as file:
                return int(file.read())
        except:
            return 0

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()
        return self.score

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
