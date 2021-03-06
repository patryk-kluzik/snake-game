from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (20, 0)]
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

    def generate_snake(self):
        for position in STARTING_POS:
            self.add_part(position)

    def add_part(self, position):
        body_part = Turtle("square")
        body_part.penup()
        body_part.color("white")
        body_part.setposition(position)
        self.snake.append(body_part)

    def grow(self):
        self.add_part(self.snake[-1].pos())

    def reset_snake(self):
        for snake_part in self.snake:
            snake_part.ht()
        self.snake.clear()
        self.generate_snake()
        self.head = self.snake[0]

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part - 1].xcor()
            new_y = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(x=new_x, y=new_y)
            # print(f"Snake part at index {snake_part} is at", self.snake[snake_part].position())
        self.head.fd(MOVE_DISTANCE)
        # print(f"While head is at index :", self.head.position())
