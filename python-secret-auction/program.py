import os


stop = False

# While loop that captures information for bidding while stop is equal to False.
while stop == False:
    name = input("What is your name?:")
    bid = input("What is your bid?: $")
    condition = input("Are there any other bidders?:\n").lower()
    # Clears operating system.
    os.system('clear')
    # switches while loop off. 
    if condition == 'no':
        stop = True


