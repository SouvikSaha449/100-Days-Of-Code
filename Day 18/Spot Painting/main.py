# import colorgram
import turtle
import random

#
# colors = colorgram.extract("image.png", 10)
# color = []
# for colour in colors:
#     r = colour.rgb.r
#     b = colour.rgb.b
#     g = colour.rgb.g
#     new_color = (r, b, g)
#     color.append(new_color)
#
# print(color)
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(235, 211, 228), (104, 125, 106), (213, 91, 152), (140, 150, 140), (186, 32, 62), (225, 109, 212),
              (199, 173, 147), (237, 225, 215), (105, 170, 112)]


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
