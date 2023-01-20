import random
# Word list 
word_list = ["hired", "wealthy", "magic", "love", "dance"]

# generate a random word. 
random_word = random.choice(word_list)

guess = input("Guess a letter.\n")

output = ""
for char in random_word:
    output += '_'
print(output)






if guess in random_word:
    pass
