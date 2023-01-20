import random
# Word list 
word_list = ["hired", "wealthy", "magic", "love", "dance"]

# generate a random word. 
random_word = random.choice(word_list)


guess = input("Guess a letter.\n")

for char in random_word:
    if guess == char:
        print("right")
    else:
        print("wrong")


    
