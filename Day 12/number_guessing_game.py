#Task 1: Print the logo number guessing game
#Task 2:Randomly choose a number between 1 and a 100

import random
import goto




def rand_number():
    return random.randint(1, 100)
#Task 3:- Create a function check that will print out too high if the user's guess is greater than the chosen number or will print out too low if the user's guess is less than the chosen number 

#user guess will be num1 and random number will be num2
def check(num1,num2):
    if  num1 == num2:
        return 0
    elif  num1 < num2:
        return 1
    else:
        return 2


print("Number Guessing Game")
random_number = rand_number()
print(f"I am thinking of a number between 1 to 100")
dificulty = input("Choose your dificulity easy, medium or hard: ").lower()
if dificulty == "easy":
    lives=10
elif dificulty == "medium":
    lives = 8
elif dificulty == "hard":
    lives=5
else:
    print("Invalid Input! Exiting the game. ")
    exit()  

print(f"You have {lives} attempts to guess the number")
while lives> 0:
    
    user_number = int(input("Enter your guess: "))
    result=check(num1=user_number,num2=random_number)
    if  result==0:
        print("Congratulations! You got it right.")
        break
    elif result==1:
        print("Too Low")
        lives-=1
        if lives == 0:
            print(f"The number was {random_number}")
            print("You have run out of attempts! You have lost")
            break
        print(f"You have {lives} attempts left")
    else:
        print("Too High")
        lives-=1
        if lives == 0:
            print("You have run out of attempts! You have lost")
            break
        print(f"You have {lives} attempts left")
    
    


    
