from turtle import Turtle, Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen=Screen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
snake.up()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    scoreboard.Score()
    def increaseScore():
        scoreboard.score += 1
        scoreboard.Score()

    #detect snake collision with the food.
    if snake.head.distance(food)<15:
        print("nom nom nom")
        food.refresh()
        increaseScore()
        snake.extend()

    if snake.head.xcor()< -287 or snake.head.xcor() > 287 or snake.head.ycor() <-287 or snake.head.ycor() >287:
        # game_is_on=False
        # scoreboard.gameOver()
        scoreboard.resetScoreboard()
        snake.snakeReset()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head)<10:
            # game_is_on=False
            # scoreboard.gameOver()
            scoreboard.resetScoreboard()
            snake.snakeReset()





screen.exitonclick()