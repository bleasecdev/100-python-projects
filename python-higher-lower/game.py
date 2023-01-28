import art
import game_data
import random
import os

# print(len(game_data.data))



# Create a function that will grab the name, follower count,
# and country from a random item in the data dictionary. 
points = 0

def get_data():
    dict = game_data.data[random.randint(0,49)]
    celeb_info = []
    for celebrity_data in dict.values():
        celeb_info.append(celebrity_data)
    return celeb_info

A = get_data()
B = get_data()
playing = True

def game(info1, info2):
    global points
    global playing
    while playing:
        def user_choice(data_a, data_b):
            print(art.logo)
            print(f"Compare A: {data_a[0]} a {data_a[2]}, from {data_a[3]}")
            print(art.vs)
            print(f"Compare B: {data_b[0]} a {data_b[2]}, from {data_b[3]}")
            print(f"You currently have {points} point(s)")
            choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if choice == 'A':
                return data_a
            if choice == 'B':
                return data_b

        choice = user_choice(info1, info2)


        # Create a function that compares two sets of celebrity information
        # and returns the greater value

        def compare(data_a2, data_b2):
            global A
            global B
            if data_a2 == data_b2:
                compare(A, B)
            if data_a2[1] > data_b2[1]:
                A = data_a2
            if data_b2[1] > data_a2[1]:
                A = data_b2
            return A

        correct = compare(info1, info2)



        # Create a function that will allow the user to play the again, 
        # until they guess wrong.  
        if choice == correct:
            points += 1
            os.system('clear')
            A = correct
            B = get_data()
            game(A, B)
        if choice != correct:
            print(f"You scored {points} point(s), Thanks for playing.")
            playing = False


game(A, B)






