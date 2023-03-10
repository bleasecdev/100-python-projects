import program_art

# program art
print(program_art.logo)

#alphabet
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 
's','t', 'u', 'v', 'w', 'x', 'y', 'z']

# Variable that controls the while loop. 
again = True

# Encryption function
def encryption(message, shift_num):
    output = []
    for char in message:
        if char in letters:
            output.append(letters[letters.index(char) + shift_num])
        else: output.append(char)    
        code = "".join(output)
    print(f"Here is your encoded message: {code}")

# Decryption function
def decryption(message, shift_num):
    output = []
    for char in message:
        if char in letters:
            output.append(letters[letters.index(char) - shift_num])
        else:
            output.append(char)
        decode = "".join(output)
    print(f"Here is your decoded message: {decode}")

# While loop containg program logic. 
while again == True:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift_num = int(input("Type shift number:\n"))
    shift_num = shift_num % 26

    if command == 'encode':   
        encryption(message, shift_num)
    if command == 'decode':
        decryption(message, shift_num)
    else:
        ValueError

    decision = input("Type 'yes' if you would like to go again otherwise type 'no'.\n")

    if decision == 'no':
        again = False
    else:
        again = True



