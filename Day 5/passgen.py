#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
choose=str(input("Type C:If You Want To Choose The Number Of Letters,Symbols And Numbers.\nType G If You Want The Password Generator To Choose For You\n"))

if(choose=="C"):
    nr_letters= int(input("How Many Letters Would You Like In Your Password?\n")) 
    nr_symbols = int(input(f"How Many Symbols Would You Like?\n"))
    nr_numbers = int(input(f"How Many Numbers Would You Like?\n"))
    nr_choice = str(input(f"Choose E for Easy And H for Hard.\nNote:In Easy Password The Order Of The Password Is Not Randomized.In Hard The Order Of The Password Is Also Randomized\n")) 

    if nr_choice=="E":
    # Easy 

        password = ""

        for char in range(1,nr_letters+1):
            random_character=random.choice(letters)  
            password+=random_character

        for sym in range(1,nr_symbols+1):
            random_symbol=random.choice(symbols)
            password+=random_symbol

        for  num in range(1, nr_numbers + 1):
            random_number = random.choice(numbers)
            password+= random_number

        print(f"Your Password Is {password}")

    elif nr_choice == "H":
        #hard
        password_list = []

        for char in range(1,nr_letters+1):
            random_character=random.choice(letters)  
            password_list+=random_character

        for sym in range(1,nr_symbols+1):
            random_symbol=random.choice(symbols)
            password_list+=random_symbol

        for  num in range(1, nr_numbers + 1):
            random_number = random.choice(numbers)
            password_list+= random_number

        # print(password_list)
        random.shuffle(password_list)
        #print(password_list)
        password = ""
        
        for char in password_list:
            password+=char

        print(f"Your Password Is {password}")

if choose == "G":
    nr_letters= random.randint(1,5)
    nr_symbols = random.randint(1,4)
    nr_numbers = random.randint(1,6)


#hard
    password_list = []

    for char in range(1,nr_letters+1):
        random_character=random.choice(letters)  
        password_list+=random_character

    for sym in range(1,nr_symbols+1):
        random_symbol=random.choice(symbols)
        password_list+=random_symbol

    for  num in range(1, nr_numbers + 1):
        random_number = random.choice(numbers)
        password_list+= random_number

    # print(password_list)
    random.shuffle(password_list)
    #print(password_list)
    password = ""
        
    for char in password_list:
        password+=char

    print(f"Your Password Is {password}")






