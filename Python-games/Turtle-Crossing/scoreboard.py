FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.speed("fastest")
        self.goto(-280,260)
        self.write(f"Level = {score}", True,"left",FONT)

    def level(self,score):
        score +=1
    def clear1(self):
        self.clear()

    def game_over(self):
        self.hideturtle()
        self.teleport(0,0)
        self.write("Game Over.", True, "center", FONT)

    def win(self):
        self.hideturtle()
        self.teleport(0, 0)
        self.write("You Won.", True, "center", FONT)