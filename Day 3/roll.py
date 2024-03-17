print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if(height>=120):
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age<=18:
        bill= 7
        print(f"Youth tickets are ${bill}")
    else:
        bill= 10
        print(f"Adult tickets are ${bill}")
    wants_photo = input("Do you want your photo taken Y or N?")
    if wants_photo == "Y":
        bill+=4
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("Sorry you are not tall enough for the rollercoaster")