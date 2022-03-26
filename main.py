from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2
MAX_Y = SCREEN_HEIGHT / 2
PADDING = 20
STARTING_TIME_DELAY = 0.15
LOWEST_TIME_DELAY = 0.05

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

controls = {
    "arrows": ['Up', 'Left', 'Down', 'Right'],
    "wasd": ["w", "a", "s", "d"]
}

controls_choice = screen.numinput(title="Choose your controls", prompt="Type (1) for Arrows or (2) for 'WASD'",
                                  default=1, minval=1, maxval=2)

if controls_choice == 1:
    game_controls = controls["arrows"]
else:
    game_controls = controls["wasd"]

snake = Snake()

screen.listen()
screen.onkey(fun=snake.go_up, key=game_controls[0])
screen.onkey(fun=snake.go_left, key=game_controls[1])
screen.onkey(fun=snake.go_down, key=game_controls[2])
screen.onkey(fun=snake.go_right, key=game_controls[3])

food = Food(max_x=MAX_X, max_y=MAX_Y)
score = Score(max_y=MAX_Y)
current_score = score.score
game_over = False

time_delay = 0.06
while not game_over:
    screen.update()
    time.sleep(time_delay)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 10:
        food.new_food(max_y=MAX_Y, max_x=MAX_X)
        current_score = score.update_score()

        snake.grow()
        if current_score % 5 == 0 and time_delay >= LOWEST_TIME_DELAY:
            time_delay -= .01

    # detect collision with wall (game over)
    if snake.head.xcor() > MAX_X - PADDING or snake.head.xcor() < -MAX_X + PADDING \
            or snake.head.ycor() > MAX_Y - PADDING or snake.head.ycor() < -MAX_Y + PADDING:
        game_over = True
        score.game_over()

    #detect collision with tail
    for snake_part in snake.snake[1:]:
        if snake.head.distance(snake_part) < 10:
            print(snake.head.distance(snake_part))
            game_over = True
            score.game_over()


screen.exitonclick()
