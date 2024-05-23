# Adding unlimited arguments

def add(*args):
    addition = 0
    for element in args:
        addition += element

    print(addition)


add(12, 8, 9, 5, 6)


# Kwargs or keyword arguments

def calculate(n, **kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["mul"]
    return n


print(calculate(0, add=5, mul=6))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Honda")
print(my_car.make)

# args is a tuple
# kwargs is a dictionary
