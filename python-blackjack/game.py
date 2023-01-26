import random
import art


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10]

play = input("Do you want to play Blackjack? Type 'y' or 'n': ")

your_cards = [random.choice(cards), random.choice(cards)]
computers_cards = [random.choice(cards), random.choice(cards)]

if play == 'y':
    print(art.logo)
    print(f"Your cards: {your_cards}")
    print(f"Computer's first card: {computers_cards[0]}")
    input("Type 'y' to get another card, type 'n' to pass: ")



