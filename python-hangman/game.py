import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Word list 
word_list = ["hired", "wealthy", "magic", "love", "dance"]

# generate a random word. 
random_word = random.choice(word_list)

end_of_game = False

display = []

lives = 6

def print_stages(stage):
    print(stages[stage])




print_stages(lives)

print(random_word)


for _ in range(len(random_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    # Ask the user to guess a letter.  
    guess = input("Guess a letter:").lower()
#Check if the letter the user guessed is in the word
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True     
        print("You win.")
    



