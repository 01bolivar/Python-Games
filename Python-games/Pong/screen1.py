import time
from turtle import Turtle, Screen
from ball import Ball, Paddle
score1 = 0
score2 = 0


# noinspection PyGlobalUndefined
class Screen1:
    def __init__(self):
        screen = Screen()
        screen.clear()
        screen.listen()
        screen.tracer(0)
        p = Paddle()
        b = Ball(p)
        screen.bgcolor("black")
        screen.setup(1500,800)
        screen.update()
        score = Turtle()
        score.hideturtle()
        screen.title("Pong Game")
        score.pu()
        score.pencolor("white")
        score.goto(0,340)
        score.write(f"{score2}    {score1}",True,"center",("arial",40,"normal"))
        middle = Turtle()
        middle.hideturtle()
        middle.pencolor("white")
        middle.pu()
        middle.goto(0,-400)
        middle.setheading(90)
        middle.pensize(5)
        for r in range(60):
            middle.pd()
            middle.forward(10)
            middle.pu()
            middle.forward(10)
        screen.onkey(p.go_up, "Up")
        screen.update()
        screen.onkey(p.go_down, "Down")
        screen.update()
        screen.onkey(p.go_up1, "w")
        screen.update()
        screen.onkey(p.go_down1, "s")
        screen.update()
        game = True
        s = Score()
        while game:
            b.move()
            time.sleep(0.04)
            screen.update()
            if b.xcor()>750:
                s.score_2()
                j = Screen1()
            if b.xcor()<-750:
                s.score_1()
                m = Screen1()
            if score2==5 or score1==5:
                if score1==5:
                    screen.clear()
                    score.write(f"Player 1 Has Won {score1} - {score2} ", True, "center", ("arial", 40, "normal"))
                    screen.update()
                    time.sleep(5)
                else:
                    screen.clear()
                    score.write(f"Player 2 Has Won {score2} - {score1} ", True, "center", ("arial", 40, "normal"))
                    screen.update()
                    time.sleep(5)
                game = False


        screen.exitonclick()

class Score:
    def __init__(self, ball = None):
        super().__init__()
    def score_1(self):
        global score1
        score1 += 1
    def score_2(self):
        global score2
        score2 += 1






i = Screen1()

