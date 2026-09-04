import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
score = 1
speed = 1
screen.setup(width=600, height=600)
screen.listen()
p = Player()
s = Scoreboard(score)
screen.tracer(0)
c = CarManager()
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    screen.onkey(p.move, "Up")
    c.create()
    c.move()
    if p.ycor()>280:
        s.clear1()
        p.teleport(0,-280)
        score+=1
        s = Scoreboard(score)
        c.increment()
        screen.update()
    for car in c.cars:
        if p.distance(car)<20:
            screen.clear()
            s = Scoreboard(score)
            s.game_over()
            screen.update()
            time.sleep(2)
            game_is_on=False
    if score == 6:
        screen.clear()
        s.win()
        screen.update()
        time.sleep(2)
        game_is_on = False
    time.sleep(0.1)
    screen.update()
