from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        import random
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
