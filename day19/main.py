from turtle import Turtle, Screen

# Task 1

# niko = Turtle()
# niko.pendown()
#
#
# def move_forward():
#     niko.fd(10)
#
#
# def move_backwards():
#     niko.backward(10)
#
#
# def turn_left():
#     niko.left(30)
#
#
# def turn_right():
#     niko.right(30)
#
#
# screen = Screen()
# screen.listen()
#
# screen.onkeypress(move_forward, 'w')
# screen.onkeypress(move_backwards, 's')
# screen.onkeypress(turn_right, 'd')
# screen.onkeypress(turn_left, 'a')
# screen.onkeypress(niko.clear, 'c')
# screen.onkeypress(niko.home, 'h')
# screen.exitonclick()
#
#

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Enter a colour:")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# niko = Turtle()
# niko.shape("turtle")
# niko.penup()
# niko.goto(x=-240, y=0)
y = -190 - (380 / len(colours))
for colour in colours:
    y += 380 / len(colours)
    turtle_colour = colour
    colour = Turtle()
    colour.color(turtle_colour)
    colour.shape('turtle')
    colour.penup()
    colour.goto(x=-240, y=y)


screen.exitonclick()