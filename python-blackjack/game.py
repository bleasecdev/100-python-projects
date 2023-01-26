import random
import art
import os

# Function that deals cards.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10]
    card = random.choice(cards)
    return card

# Function that calculates the score of each players hand.
def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return(sum(cards))

# Function that compares each players hands and determines a win, lose, or draw. 
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with Blackjack"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win!"
    else: return "You Lose."

# Function that runs the game and all of it's logic. 
def play_game():

    print(art.logo)

    your_cards = []
    computers_cards = []
    is_game_over = False

    for _ in range(2):
        your_cards.append(deal_card())
        computers_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(your_cards)
        computer_score = calculate_score(computers_cards)
        print (f"Your cards: {your_cards}")
        print(f"Computer's first card: {computers_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again == 'y':
                your_cards.append(deal_card())
            else: 
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card)
        computer_score = calculate_score(computers_cards)

    print(f"Your final hand: {your_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    #Hint 14: Ask the user if they want to restart the game. If they answer yes, 
    # clear the console and start a new game of blackjack and show the logo from art.py.
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('clear')
        play_game()

play_game()






