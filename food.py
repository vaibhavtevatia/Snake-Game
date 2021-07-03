from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        # self.goto(random.randint(-290,290),random.randint(-290,290))
        self.update_location()
    def update_location(self):
        self.goto(random.randint(-260,260),random.randint(-260,260))
