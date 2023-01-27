import art
import game_data
import random

print(len(game_data.data))



# Create a function that will grab the name, follower count,
# and country from a random item in the data dictionary. 
celeb_info_a = []
celeb_info_b = []
points = 0

def get_data():
    dict = game_data.data[random.randint(0,49)]
    for celebrity_data in dict.values():
        celeb_info_a.append(celebrity_data)
    return celeb_info_a,

def get_data_2():
    dict = game_data.data[random.randint(0,49)]
    for celebrity_data in dict.values():
        celeb_info_b.append(celebrity_data)
    return celeb_info_b
    

# Create a function taht compares two sets of celebrity information
# formated in a sentence. 

get_data()
get_data_2()

def compare(A, B):
    if A[1] > B[1]:
        return A
    else: 
        return B
    

print(compare(celeb_info_a, celeb_info_b))




# Create a function that will allow the user to play the again, 
# until they guess wrong.  

print(f"Compare A: {celeb_info_a[0]}, a {celeb_info_a[2]}, from {celeb_info_a[3]}")
print(f"Compare B: {celeb_info_b[0]}, a {celeb_info_b[2]}, from {celeb_info_b[3]}")

user_choice = input("Who has more followers? Type 'A' or 'B': ")


