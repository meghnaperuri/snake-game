from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        self.file_path="file.txt"
        super().__init__()
        self.score=0
        if os.path.exists(self.file_path):
            with open("file.txt",mode="r") as f:
                self.highScore=int(f.read())
                print(self.highScore)
                print("read")
        self.color("white")
        self.penup()
        self.goto(0,260)
        # self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.hideturtle()
        self.Score()

    def Score(self):
        self.clear()
        # score_text="score = "+ str(self.score)
        self.write(f"score = {self.score} high score: {self.highScore}", False, align="center",font=("Courier ",22,"normal"))

    def resetScoreboard(self):
        if self.score>self.highScore:
            self.highScore=self.score
            with open("file.txt", mode="w") as f:
                f.write(str(self.highScore))
        self.score=0
    #
    # def gameOver(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("Game over.", False, align="center",font=("Courier ",26,"normal"))
    #/Users/meghnaperuri/Desktop/python/pycharm/day-20,21/Snake Game/file.txt