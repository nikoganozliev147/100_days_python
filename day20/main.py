from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake_segments = ['niko', 'niko1', 'niko2']
snake = Snake(snake_segments)
food = Food()
game_scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        game_scoreboard.update_score()
        snake.add_segment()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 \
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False

game_scoreboard.game_over()
screen.exitonclick()
