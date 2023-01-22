import program_art

print(program_art.logo)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 
's','t', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt user for encryption or decryption. 
command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("Type your message:\n")
shift_num = input("Type shift number:\n")


def encryption(message, shift_num):
    output = []
    for char in message:
        if char in letters:
            output.append(letters.index(char))
    return output


print(encryption(message, shift_num))


