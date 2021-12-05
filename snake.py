SEGMENT_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.start()
        self.speed = 10
        self.head = self.segments[0]

    def start(self):
        x_cor = 0
        for segment in range(3):
            self.add_segment((x_cor, 0))
            x_cor -= 20

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x, y)
        self.head.forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def controls(self):
        from turtle import Screen
        s = Screen()
        s.listen()
        s.onkey(self.up, "Up")
        s.onkey(self.right, "Right")
        s.onkey(self.down, "Down")
        s.onkey(self.left, "Left")

    def add_segment(self, position):
        from turtle import Turtle
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
