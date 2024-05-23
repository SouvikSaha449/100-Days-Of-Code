from tkinter import *

window = Tk()
window.config(padx=20, pady=20)


def calculate():
    inputted = int(input_text.get())
    mk = round(inputted * 1.60934)
    third_label.config(text=mk)


input_text = Entry(width=10)
input_text.grid(column=1, row=0)

first_label = Label(text="Miles")
first_label.grid(column=2, row=0)

second_label = Label(text="is equal to")
second_label.grid(column=0, row=1)

third_label = Label(text="0")
third_label.grid(column=1, row=1)

fourth_label = Label(text="km")
fourth_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
