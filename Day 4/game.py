

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome To Rock, Paper, Scissors")

import random

list = [rock,paper,scissors]

user_choice = int(input("0 for Rock,1 for Paper,2 for Scissors:\n"))

computer_choice = random.randint(0,2)


if(user_choice>2  or user_choice<0):
    print("Invalid Input! Please enter a number between 0 to 2 only.")
elif(user_choice==computer_choice):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("It's a tie!")
        
elif(user_choice == 0 and computer_choice == 1):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Paper defeats Rock\nComputer Wins!")
        
elif(user_choice==0 and computer_choice == 2):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Rock crushes Scissors\nUser Wins!")
        
elif(user_choice==1 and computer_choice == 0):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Paper defeats Rock\nUser Wins!")
        
elif(user_choice==1 and computer_choice == 2):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Scissor cuts Paper\nComputer Wins ")
        
elif(user_choice==2 and computer_choice == 0):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Rock crushes Scissors\nComputer Wins!")
        
elif(user_choice==2 and computer_choice==1):
    print(f"You chose  {list[user_choice]}")
    print(f"Computer chose{list[computer_choice]}")
    print("Scissors cut Paper\n User Wins!")
        



