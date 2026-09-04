from turtle import Turtle
from random import  randint
class Paddle:
    def __init__(self):
        self.paddle1 = Turtle()
        self.paddle2 = Turtle()
        self.paddle1.shape("square")
        self.paddle1.color("white")
        self.paddle1.shapesize(5, 1)
        self.paddle1.pu()
        self.paddle1.goto(720, 0)
        self.paddle2.shape("square")
        self.paddle2.color("white")
        self.paddle2.shapesize(5, 1)
        self.paddle2.pu()
        self.paddle2.goto(-730, 0)
    def go_up(self):
        if self.paddle1.ycor()<=340:
            new_y = self.paddle1.ycor() + 25
            self.paddle1.goto(720, new_y)
    def go_down(self):
        if self.paddle1.ycor()>= -340:
            new_y = self.paddle1.ycor() - 25
            self.paddle1.goto(720, new_y)
    def go_up1(self):
        if self.paddle2.ycor()<=340:
            new_y = self.paddle2.ycor() + 25
            self.paddle2.goto(-730, new_y)
    def go_down1(self):
        if self.paddle2.ycor()>= -340:
            new_y = self.paddle2.ycor() - 25
            self.paddle2.goto(-730, new_y)
class Ball(Turtle):
    def __init__(self, paddle = None):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.setheading(randint(0,361))
        self.p= paddle if paddle else Paddle()
    def move(self):
        self.forward(10)
        if self.ycor()>385:
            self.setheading(360-self.heading())
        elif self.ycor()<-380:
            self.setheading(360-self.heading())
        if self.xcor() > 700 and self.distance(self.p.paddle1) < 50:
            self.setheading(180 - self.heading())
        if self.xcor() < -710 and self.distance(self.p.paddle2) < 50:
            self.setheading(180 - self.heading())





