
def calculator():
    output = None
    stop = False
    
    while stop == False:
        number = int(input("What's the first number?: "))
        print(['+', '-', '*', '/'])
        operator = input("{{Pick an operation: ")
        next_number = int(input("What is the next number?: "))
        
        if operator == '+':
            output = number + next_number
        if operator == '-':
            output = number - next_number
        if operator == '/':
            output = number / next_number
        if operator == '*':
            output = number * next-number
        
        cont = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if cont == 'n':
            print(output) 
            stop = True
        if cont == 'y':
            number = output
            stop = True

calculator()


   







