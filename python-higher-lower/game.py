import art
import game_data
import random

# print(len(game_data.data))



# Create a function that will grab the name, follower count,
# and country from a random item in the data dictionary. 
playing = True
points = 0

def get_data():
    dict = game_data.data[random.randint(0,49)]
    celeb_info = []
    for celebrity_data in dict.values():
        celeb_info.append(celebrity_data)
    return celeb_info

A = get_data()
B = get_data()

print(A, B)

while playing:
    def user_choice(data_a, data_b):
        print(f"Compare A: {data_a[0]} a {data_a[2]}, from {data_a[3]}")
        print(f"Compare B: {data_b[0]} a {data_b[2]}, from {data_b[3]}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice == 'A':
            return data_a
        if choice == 'B':
            return data_b

    choice = user_choice(A, B)

    print(choice)


    # Create a function that compares two sets of celebrity information
    # and returns the greater value

    def compare(data_a2, data_b2):
        global A
        if data_a2[1] > data_b2[1]:
            A = data_a2
        if data_b2[1] > data_a2[1]:
            A = data_b2
        return A

    correct = compare(A, B)



    # Create a function that will allow the user to play the again, 
    # until they guess wrong.  


    if choice == correct:
        points += 1
        A = correct
        user_choice(A, B)
    if choice != correct:
        playing = False








