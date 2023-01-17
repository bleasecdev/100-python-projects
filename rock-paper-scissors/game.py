import random

# program art
rock_pic = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''

paper_pic = ''' 
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' '''

scissors_pic = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''


# Greeting
print("Welcome to Rock Paper Scisors!")
# List of possible moves
moves = ["rock", "paper", "scissors"]
# Prompt player for their move
player = int(input("Choose your weapon type 0 for rock, 1 for paper, or 2 for scissors?\n"))
# Computer makes a random selection
computer = random.randint(0,2)
# Moves are printed to the console
print(f"You chose {moves[player]}")
print(f"The computer chose {moves[computer]}.")
# Game logic
if player == 0 and computer == 2:
    print("You win!")
elif player == 1 and computer == 0:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == computer:
    print("Draw")
else:
    print("You lose!")

# Artwork Logic
if player == 0:
    print("Player", rock_pic)
if player == 1:
    print("Player", paper_pic)
elif player == 2:
    print("Player", scissors_pic)

if computer == 0:
    print("Computer", rock_pic)
if computer == 1:
    print("Computer", paper_pic)
if computer == 2:
    print("Computer", scissors_pic)