from turtle import Turtle, Screen
from tkinter import messagebox

timmy = Turtle()
screen = Screen()
timmy.speed("fast")


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_right():
    timmy.right(10)


def turn_left():
    timmy.left(10)


messagebox.showinfo("How to Draw", "W to move Forward\nS to move Backward\nA for turning left\nD for turning right\nC "
                                   "to reset\nClick on the screen to exit" )
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=timmy.reset)
screen.exitonclick()
