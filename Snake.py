from turtle import Turtle, Screen
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()#remove this
        new_segment.shape("square")#and you can use "self." instead of new_segment
        new_segment.color("white")
        new_segment.turtlesize(1, 1, 1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def snakeReset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

