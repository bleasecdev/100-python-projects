import random

print("Welcome to Rock Paper Scisors")

moves = ["rock", "paper", "scissors"]

player = input("Choose your weapon rock, paper, or scissors?\n")
computer = random.choice(moves)
print(f"The computer chose {computer}.")

if player == 'rock' and computer == 'scissors':
    print("You win!") 
elif player == 'paper' and computer == 'rock':
    print("You win!")
elif player == 'scissors' and computer == 'paper':
    print("You win!")
elif player == computer:
    print("Draw")
else:
    print("You Lose")

if player == 'paper':
    print(''' PLAYER
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' ''')
elif player == 'rock':
    print(''' PLAYER
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       ''')
else:
    print(''' PLAYER
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''')

if computer == 'paper':
    print(''' COMPUTER
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' ''')
if computer == 'rock':
    print(''' COMPUTER
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       ''')
if computer == 'scissors':
    print(''' COMPUTER
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''')
