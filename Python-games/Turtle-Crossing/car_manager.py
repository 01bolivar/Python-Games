COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import choice, randint
class CarManager:
    def __init__(self):
        self.cars = []
    def create(self):
        if randint(1,6)==1:
            car = Turtle()
            car.hideturtle()
            car.setheading(180)
            car.pu()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(1, 2)
            car.speed(1)
            car.setposition(350, randint(-250, 250))
            car.showturtle()
            self.cars.append(car)
    def increment(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+=MOVE_INCREMENT
    def move(self):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE)