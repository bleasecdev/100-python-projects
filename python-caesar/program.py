import program_art

print(program_art.logo)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 
's','t', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt user for encryption or decryption. 
again = True

def encryption(message, shift_num):
    output = []
    for char in message:
        if char in letters:
            output.append(letters[letters.index(char) + int(shift_num)])
        code = "".join(output)
    print(f"Here is your encoded message: {code}")


def decryption(message, shift_num):
    output = []
    for char in message:
        output.append(letters[letters.index(char) - int(shift_num)])
        decode = "".join(output)
    print(f"Here is your decoded message: {decode}")


while again == True:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift_num = input("Type shift number:\n")

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













