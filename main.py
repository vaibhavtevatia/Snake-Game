from turtle import Screen
from food import Food
from snake import Snake
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

snake = Snake()
screen.screensize(500,500)
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")


food = Food()

scoreboard = ScoreBoard()



game_on =True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move_body()
    if snake.snakehead.distance(food) <20:
        snake.add_body(snake.snakelist[-1].pos())
        food.update_location()
        scoreboard.update_score()
    if snake.check_collision() or snake.snakehead.xcor() > 350 or snake.snakehead.xcor() < -350 or snake.snakehead.ycor() > 350 or snake.snakehead.ycor() < -350:
        scoreboard.reset_board()
        snake.send_snake()
        snake.reset_snake()

screen.exitonclick()
