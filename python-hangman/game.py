import random
import game_art
import game_words





# generate a random word. 
random_word = random.choice(game_words.word_list)

end_of_game = False

display = []

lives = 6

end_of_game = False

print(game_art.logo)
print(random_word)


for _ in range(len(random_word)):
    display += "_"
print(display)



while not end_of_game:
    game_art.print_stages(lives)
    # Ask the user to guess a letter.  
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"you already guessed {guess}")
        lives -=1

#Check if the letter the user guessed is in the word
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
            
    if "_" not in display:
        end_of_game = True     
        print("You win.")
    



