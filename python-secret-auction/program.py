import os
import art


dict = {}
stop = False

# Program Logo
print(art.logo)

# While loop that captures information for bidding while stop is equal to False.
while stop == False:
    name = input("What is your name?:")
    bid = input("What is your bid?: $")
    condition = input("Are there any other bidders?:\n").lower()

# Add key value pairs to the dictionary
    dict[name] = bid

# switches while loop off. 
    if condition == 'no':
        stop = True
        print(f"The winner of the auction is {max(dict, key = dict.get)} who bid ${dict.get(max(dict, key = dict.get))}.")
        
    if condition == 'yes':
    #  Clears operating system.
        os.system('clear')

