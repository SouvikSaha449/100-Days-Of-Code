MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1:-  Print report. a. When the user enters “report” to the prompt, a report should be generated that shows the
#  current resource values. e.g. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5

def display_resources(resource):
    water_value = resource["water"]
    milk_value = resource["milk"]
    coffee_value = resource["coffee"]
    cash_value = resource["cash"]
    print(
        f"Water Quantity: {water_value}\nMilk Quantity: {milk_value}\nCoffee Quantity: {coffee_value}\nCash: {cash_value}")


def make_coffee(resource, menu):
    if user_choice == "latte":
        resource["water"] = resource["water"] - menu["latte"]["ingredients"]["water"]
        resource["coffee"] = resource["coffee"] - menu["latte"]["ingredients"]["coffee"]
        resource["milk"] = resource["milk"] - menu["latte"]["ingredients"]["milk"]

    elif user_choice == "cappuccino":
        resource["water"] -= menu["cappuccino"]["ingredients"]["water"]
        resource["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
        resource["milk"] -= menu["cappuccino"]["ingredients"]["milk"]

    else:
        resource["water"] -= menu["espresso"]["ingredients"]["water"]
        resource["coffee"] -= menu["espresso"]["ingredients"]["coffee"]


def transaction(resource, menu):
    print("Enter your coins")
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickel = int(input("How many nickels?: "))
    user_pennies = int(input("How many pennies?: "))

    total = float((user_quarters * .25) + (user_dimes * .10) + (user_nickel * .05) + (user_pennies * .01))
    print(f"Your total is ${total}")

    if user_choice == "latte":
        if total > menu["latte"]["cost"]:
            resource["cash"] = menu["latte"]["cost"]
            make_coffee(resource, menu)
            print("Coffee is made")
            return round(total - menu["latte"]["cost"], 3)
        elif total == menu["latte"]["cost"]:
            resource["cash"] = total
            make_coffee(resource, menu)
        else:
            print("Sorry that's not enough money. Money refunded.")
            return total

    elif user_choice == "espresso":
        if total > menu["espresso"]["cost"]:
            resource["cash"] = menu["espresso"]["cost"]
            make_coffee(resource, menu)
            return round(total - menu["espresso"]["cost"], 3)
        elif total == menu["espresso"]["cost"]:
            resource["cash"] = total
            make_coffee(resource, menu)
        else:
            print("Sorry that's not enough money. Money refunded.")
            return total

    else:
        if total > menu["cappuccino"]["cost"]:
            resource["cash"] = menu["cappuccino"]["cost"]
            make_coffee(resource, menu)
            return round(total - menu["cappuccino"]["cost"], 3)
        elif total == menu["cappuccino"]["cost"]:
            resource["cash"] = total
            make_coffee(resource, menu)
        else:
            print("Sorry that's not enough money. Money refunded.")
            return total


# TODO: 2:- Prompt user by asking “What would you like? (espresso/latte/cappuccino):”a. Check the user’s input to
#  decide what to do next. b. The prompt should show every time action has completed, e.g. once the drink is
#  dispensed. The prompt should show again to serve the next customer

# TODO: 3:- Check resources sufficient? a. When the user chooses a drink, the program should check if there are enough
#  resources to make that drink. b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
#  It should not continue to make the drink but print: “Sorry there is not enough water.” c. The same should happen
#  if another resource is depleted, e.g. milk or coffee.

def check(resource, menu):
    if user_choice == "espresso":
        if resource["water"] >= menu["espresso"]["ingredients"]["water"]:
            if resource["coffee"] >= menu["espresso"]["ingredients"]["coffee"]:
                print("All resources are ok")
                return True

            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough water")
            return False

    elif user_choice == "latte":
        if resource["water"] >= menu["latte"]["ingredients"]["water"]:
            if resource["coffee"] >= menu["latte"]["ingredients"]["coffee"]:
                if resource["milk"] >= menu["latte"]["ingredients"]["milk"]:
                    print("All resources are ok")
                    return True
                else:
                    print("Sorry there is not enough milk")
                    return False
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough water")
            return False

    else:
        if resource["water"] >= menu["cappuccino"]["ingredients"]["water"]:
            if resource["coffee"] >= menu["cappuccino"]["ingredients"]["coffee"]:
                if resource["milk"] >= menu["cappuccino"]["ingredients"]["milk"]:
                    print("All resources are ok")
                    return True
                else:
                    print("Sorry there is not enough milk")
                    return False
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough water")
            return False


user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
Check = check(resources, MENU)
if Check:
    change = transaction(resources, MENU)
    make_coffee(resources, MENU)
    print(f"Your Change is {change}")

display_resources(resources)

# TODO: 4:- Process coins. a. If there are sufficient resources to make the drink selected, then the program should
#  prompt the user to insert coins. b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05,
#  pennies = $0.01 c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel,
#  2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# TODO: 5:- Check transaction successful?a. Check that the user has inserted enough money to purchase the drink they
#  selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say
#  “Sorry that's not enough money. Money refunded.”. b. But if the user has inserted enough money, then the cost of
#  the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered.
#  E.g. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5 c. If the user has inserted too much money, the machine
#  should offer change.

# TODO: 6:- Make Coffee. a. If the transaction is successful and there are enough resources to make the drink theuser
#  selected, then the ingredients to make the drink should be deducted from the coffee machine resources. E.g. report
#  before purchasing latte: Water: 300ml Milk: 200ml Coffee: 100g Money: $0 Report after purchasing latte: Water:
#  100ml Milk: 50ml Coffee: 76g Money: $2.5 b. Once all resources have been deducted, tell the user “Here is your
#  latte. Enjoy!”. If latte was their choice of drink.


# TODO: 7:- Turn off the Coffee Machine by entering “off” to the prompt.a. For maintainers of the coffee machine,


#  they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
