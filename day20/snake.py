from turtle import Turtle, Screen

screen = Screen()


class Snake:
    def __init__(self, segments):
        self.segments = []
        self.position = 0
        self.create_snake(segments)

    def create_snake(self, snake_segments):
        for segment in snake_segments:
            segment = Turtle('square')
            segment.penup()
            segment.color('white')
            segment.goto(x=self.position, y=0)
            self.position -= 20
            self.segments.append(segment)
        screen.update()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor())
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segment(self):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)