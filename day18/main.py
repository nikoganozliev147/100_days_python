from turtle import Turtle, Screen
import random

# Challenge 1

#     niko_the_turtle = Turtle()
#     niko_the_turtle.shape("turtle")
#     for i in range(4):
#         niko_the_turtle.fd(100)
#         niko_the_turtle.right(90)
#
#     screen = Screen()
#     screen.exitonclick()

# Challenge 2

# niko = Turtle()
# niko.shape("turtle")
# for i in range(10):
#     niko.pendown()
#     niko.fd(10)
#     niko.penup()
#     [x, y] = niko.position()
#     niko.goto(x + 10, y)
#
# screen = Screen()
# screen.exitonclick()


# Challenge 3

# niko = Turtle()
# niko.shape("turtle")
# niko.speed(0)
# for i in range(3, 10):
#     angle = 360 / i
#     for m in range(i):
#         niko.fd(100)
#         niko.right(angle)
#
# screen = Screen()
# screen.exitonclick()

# Challenge 4

# niko = Turtle()
# niko.shape("turtle")
# niko.speed(0)
# niko.pensize(10)
#
# colors = [
#     "red", "blue", "green", "yellow", "orange", "purple",
#     "pink", "brown", "gray", "black", "white", "cyan",
#     "magenta", "lime", "olive", "teal", "navy", "maroon",
#     "gold", "silver", "violet", "indigo", "turquoise",
#     "coral", "orchid", "salmon", "peru", "khaki"
# ]
#
# while True:
#     niko.setheading(random.randint(0, 360))
#     niko.pencolor(random.choice(colors))
#     niko.fd(50)

# Challenge 5

# niko = Turtle()
# niko.shape("turtle")
# niko.speed(0)
#
# colors = [
#         "red", "blue", "green", "yellow", "orange", "purple",
#         "pink", "brown", "gray", "black", "white", "cyan",
#         "magenta", "lime", "olive", "teal", "navy", "maroon",
#         "gold", "silver", "violet", "indigo", "turquoise",
#         "coral", "orchid", "salmon", "peru", "khaki"
# ]
#
# radius = 100
# for i in range(5, 355, 5):
#     niko.setheading(i)
#     niko.pencolor(random.choice(colors))
#     niko.circle(radius)
#
# screen = Screen()
# screen.exitonclick()
