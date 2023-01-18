import random 

## My Original Solution

# Establish lists containg useable data 
letters = ['a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = ['$','#','%','&','*','!','@','+','(',')']

# Greeting
print("Welcome to the Password Generator")
# Collect information from user
num_of_letters = input("How many letters would you like in your password?\n")

num_of_symbols = input("How many sybols would you like in your password?\n")

num_of_numbers = input("How many numbers would you like in your password?\n")
#Establish an output
output = ""

# Loops that select the number of characters randomly
i = 0

while i < int(num_of_letters):
    output += letters[random.randint(0, 25)]
    i += 1
i = 0

while i < int(num_of_symbols):
    output += symbols[random.randint(0,6)]
    i+= 1
i = 0

while i < int(num_of_numbers):
    output += str(random.randint(0,9))
    i += 1

#randomize the generated symbols in list format
shuffled_list = random.sample(output, k= int(len(output)))

# Join list and save to variable password 
password = "".join(shuffled_list)

# Returns the password to the user
print(f"Your password is: {password}")



