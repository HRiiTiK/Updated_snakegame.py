import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(800, 700)
screen.bgcolor('black')
screen.tracer(0)
screen.title("SNAKE GAME")

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
