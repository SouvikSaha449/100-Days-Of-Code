print("Welcome to the tip calculator")

bill=float(input("What was the total bill?"))

tip = int(input("How much would you like the tip to be? 10, 12 or 15?"))

people = int(input("How many people are sharing the bill?"))

tip1= tip/100
tip2=tip1*bill
tot1 = bill+tip2
per_person = tot1/people
roundoff = round(per_person,2)
final = "{:.2f}".format(per_person)

print(f"Each person should pay: ${final} ")