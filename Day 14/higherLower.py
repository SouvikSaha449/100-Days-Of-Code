import art
from gamedata import data
import random
import os


def formated(account):
    """Formats the dictionary in the way we want to print it"""
    acc_name = account['name']
    acc_desc = account['description']
    acc_country = account['country']

    return f"{acc_name}, A {acc_desc}, From {acc_country}"


def check(guess, firsthand_followers, secondhand_followers):
    """Check if a guess is correct and return true otherwise returns false"""
    if firsthand_followers > secondhand_followers:
        return guess == "a"
    else:
        return guess == "b"


print(art.logo)
score = 0
continue_play = True
account2 = random.choice(data)

while continue_play:
    # generating a random account

    account1 = account2
    account2 = random.choice(data)

    while account1 == account2:
        account2 = random.choice(data)

    print(f"Compare A: {formated(account1)}")
    print(art.vs)
    print(f"Against B: {formated(account2)}")

    # printing the values in a format

    guess = input("Who has more followers A or B? ").lower()

    acc1_followers = account1["follower_count"]
    acc2_followers = account2["follower_count"]
    is_Correct = check(guess, firsthand_followers=acc1_followers, secondhand_followers=acc2_followers)
    os.system('cls')
    print(art.logo)

    if is_Correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        continue_play = False
        print(f"Better luck next time. Your final score was {score}")
