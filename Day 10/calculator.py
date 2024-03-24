from art import logo

print(logo)

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():

    num1 = float(input("Enter the first number: "))

    should_continue = True
    while should_continue:

        for key in operations:
            print(key)

        operation_symbol = input("Choose an operation: ").lower()

        num2 = float(input("Enter the next number: \n"))

        calculating_function =  operations[operation_symbol]
        answer = calculating_function(num1,num2)

        print(f"{num1}{operation_symbol}{num2}={answer}")

        choice = input(f"\n Type y to continue calculating with {answer} or Type n to start a fresh calculation and type anything else to exit the calculator: ")
        if choice == "y":
            num1=answer
        elif choice == "n":
            calculator()
        else:
            should_continue = False
        
calculator()
