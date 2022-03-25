from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.50, stretch_wid=0.50)
        self.speed("fastest")
        x_axis = random.randrange(start=-280, stop=280, step=20)
        y_axis = random.randrange(start=-280, stop=280, step=20)
        self.goto(x=x_axis, y=y_axis)
