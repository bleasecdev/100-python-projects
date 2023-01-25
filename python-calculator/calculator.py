import art

print(art.logo)

   
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2,

def div(n1, n2):
    return n1/n2,

def mul(n1, n2):
    return n1 * n2, 

operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul
}

def calculator():

    n1 = int(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for key in operations.keys():
            print(key)

        operation_symbol = input("Pick an operation from the line above: ")
        n2 = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)


        print(f"{n1} {operation_symbol} {n2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()


