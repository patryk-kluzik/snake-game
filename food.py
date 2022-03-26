from turtle import Turtle
import random

PADDING = 20


class Food(Turtle):

    def __init__(self, max_x, max_y):
        super().__init__(shape="circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.50, stretch_wid=0.50)
        self.speed("fastest")
        self.new_food(max_x=max_x, max_y=max_y)

    def new_food(self, max_x, max_y):
        x_axis = random.randrange(start=-max_x + PADDING, stop=max_x - PADDING, step=20)
        y_axis = random.randrange(start=-max_y + PADDING, stop=max_y - PADDING, step=20)
        self.goto(x=x_axis, y=y_axis)
