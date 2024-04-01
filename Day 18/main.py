from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.setup(1368, 768)


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    timmy.color(r, g, b)


# timmy.shape("turtle")
# timmy.color("aquamarine3")

# Drawing a square


# Drawing a dashed line
# for _ in range(20):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()


# timmy.left(90)
# timmy.penup()
# timmy.forward(150)
# timmy.right(90)
# timmy.pendown()

# Drawing from triangle to decagon

# change_color()
# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120)
#
# change_color()
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# change_color()
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72)
#
# change_color()
# for _ in range(6):
#     timmy.forward(100)
#     timmy.right(60)
#
# change_color()
# for _ in range(7):
#     timmy.forward(100)
#     timmy.right(51.42)
#
# change_color()
# for _ in range(8):
#     timmy.forward(100)
#     timmy.right(45)
#
# change_color()
# for _ in range(9):
#     timmy.forward(100)
#     timmy.right(40)
#
# change_color()
# for _ in range(10):
#     timmy.forward(100)
#     timmy.right(36)

# Changing the pensize and speed of the turtle
timmy.pensize(2)
timmy.speed("fastest")

# Drawing a random walk with a random colour
# direction = [0, 90, 180, 270]
#
# for _ in range(150):
#     change_color()
#     timmy.forward(40)
#     timmy.setheading(random.choice(direction))

for i in range(72):
    change_color()
    timmy.circle(100)
    timmy.right(5)

screen.exitonclick()
