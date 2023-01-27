import art
import game_data
import random

print(len(game_data.data))



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

print(A, B)

# Create a function that compares two sets of celebrity information
# and returns the greater value

def compare(data_a, data_b):
    global A
    if data_a[1] > data_b[1]:
        A = data_a
    if data_b[1] > data_a[1]:
        A = data_b
    return A

correct = compare(A, B)

print(correct)



# Create a function that will allow the user to play the again, 
# until they guess wrong.  



# user_choice = input("Who has more followers? Type 'A' or 'B': ")


