import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="Guess The Next State").title()
    if answer == "Exit":
        remaining_state = [state for state in all_states if state not in guessed_state]

        state_dict = {
            "states": remaining_state
        }
        data2 = pandas.DataFrame(state_dict)
        data2.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        if answer not in guessed_state:
            guessed_state.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)




