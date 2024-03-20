# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    name="Souvik Saha"
    print("Hello")
    print(f"My Name Is {name}")
    print("Nice To Meet You")

greet()

def greet(name):
    print(f"Hello {name}")
    print(f"My Name Is {name}")
    print("Nice To Meet You")

greet("Souvik")

#Function with more than 1 input

def greet_with_location(name,location):
    print(f"I'm {name} From {location}.")

greet_with_location("Souvik","Kolkata")


#Function with keyword argument

def greet_with_location(name,location):
    print(f"I'm {name} From {location}.")

greet_with_location(location="Kolkata",name="Souvik")