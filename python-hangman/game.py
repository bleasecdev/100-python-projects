import random
import game_art
import game_words

# generate a random word from the word list in the game_words file. 
random_word = random.choice(game_words.word_list)

#Declare variables that will be used within the while and loops.  
end_of_game = False
display = []
lives = 6
end_of_game = False

# Prints the game logo to the console.
print(game_art.logo)

# This loop displays the word disguised as '_'.
for _ in range(len(random_word)):
    display += "_"
print(display)


# Game logic 
while not end_of_game:
    # prints hangman figure
    game_art.print_stages(lives)
    # Ask the user to guess a letter.  
    guess = input("Guess a letter:").lower()
    # condition that prevents the program from allowing multiple entries of the same letter.
    if guess in display:
        print(f"you already guessed {guess}. You lose a life.")
        lives -=1

#Check if the letter the user guessed is in the word.
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

# Condition for loss.
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            print(random_word)
# Condition for victory.   
    if "_" not in display:
        end_of_game = True     
        print("You win.")
    



