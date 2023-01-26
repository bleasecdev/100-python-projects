import random


num_of_lives = 0
computers_num = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    num_of_lives = 10
else:
    num_of_lives = 5


while num_of_lives > 0:
    print(f"You have {num_of_lives} attempts remaining to guess the number." )
    guess = int(input("Make a guess: "))
    if guess != computers_num:
        num_of_lives -= 1
    if guess > computers_num:
        print("Too High.")
    if guess < computers_num:
        print("Too low.")
    if guess == computers_num:
        print(f"You guessed correctly! I was thinking {computers_num}")
        break


if num_of_lives == 0:
    print(f"You ran out of guesses. My number was {computers_num}. You suck.")


