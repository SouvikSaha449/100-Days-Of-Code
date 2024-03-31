from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

is_On = True

while is_On:
    options = menu.get_items()
    user_choice = input(f"To Switch off the machine press off \nTo see the amount of ingredients press report\nWhat "
                        f"would you like? {options}\nUser Choice:  ").lower()
    if user_choice == "off":
        is_On = False
    elif user_choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
