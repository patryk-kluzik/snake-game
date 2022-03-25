from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

game_over = False

snake = Snake()

controls = {
    "arrows": ['Up', 'Left', 'Down', 'Right'],
    "wasd": ["w", "a", "s", "d"]
}

controls_choice = screen.numinput(title="Choose your controls", prompt="Type (1) for Arrows or (2) for 'WASD'",
                                  default=1, minval=1, maxval=2)

if controls_choice == 1:
    game_controls = controls["arrows"]
elif controls_choice == 2:
    game_controls = controls["wasd"]
else:
    exit()
screen.listen()
screen.onkey(fun=snake.go_up, key=game_controls[0])
screen.onkey(fun=snake.go_left, key=game_controls[1])
screen.onkey(fun=snake.go_down, key=game_controls[2])
screen.onkey(fun=snake.go_right, key=game_controls[3])

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

"""
headings : 0 east 90 north 180 west 270 south
"""

screen.exitonclick()
