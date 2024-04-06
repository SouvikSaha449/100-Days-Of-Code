class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("It can breathe")


# Inheritance in python
class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Its swimming")


nemo = Fish()
nemo.swim()
nemo.breathe()
