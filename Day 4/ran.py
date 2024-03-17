import random

# randint(a, b)
# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

random_interger = random.randint(1,10)

print(random_interger)

# random.random() -> Returns the next random floating point number between [0.0 to 1.0)
# random.uniform(a, b) -> Returns a random floating point N such that a <= N <= b if a <= b and b <= N <= a if b < a.

random_float = random.random()

random_float2 = random.uniform(0,6)

print(random_float)
print(random_float2)

fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]

vegetables= ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits,vegetables]

print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

print(dirty_dozen[1][1])