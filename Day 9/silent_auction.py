import os
import art

print(art.logo)

auction={}

choice = "yes"

def highest_bidder():    
    max_bid = 0
    winner=""
    for name in auction:
        if max_bid < auction[name]:
            max_bid = auction[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${max_bid}")

while choice=="yes":

    name = input("Enter Your Name: ")
    bid = int(input("Enter your bid: $"))
    auction[name] = bid
    choice = input("Are There Any Other Bidders? Type yes or no\n").lower()
    if choice == "no":
        os.system('cls')
        highest_bidder()
    elif choice == "yes":
        os.system('cls')
    else:
        print("Invalid Input")
    
    
