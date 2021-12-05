from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hscore = self.read_hscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scores()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :(", False, align=ALIGNMENT, font=FONT)

    def update_scores(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.hscore} ", False, align=ALIGNMENT, font=FONT)

    @staticmethod
    def read_hscore():
        with open('data.txt', 'r') as data:
            return int(data.read())

    @staticmethod
    def write_hscore(score):
        with open('data.txt', 'w') as data:
            data.write(str(score))

    def increase_score(self):
        if self.hscore <= self.score:
            self.hscore += 1
            self.score += 1
            self.write_hscore(self.score)
        else:
            self.score += 1
        self.update_scores()
        