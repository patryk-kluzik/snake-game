from turtle import Turtle

STARTING_POS = [(-20, 0), (0, 0), (20, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake = []
        self.generate_snake()
        self.head = self.snake[0]

    def generate_snake(self):
        for position in STARTING_POS:
            body_part = Turtle("square")
            body_part.color("white")
            body_part.setposition(position)
            self.snake.append(body_part)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part - 1].xcor()
            new_y = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(x=new_x, y=new_y)
        self.snake[0].fd(MOVE_DISTANCE)
