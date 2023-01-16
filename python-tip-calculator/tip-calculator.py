
# Greeting
print("Welcome to the tip calculator.")
# Captures the total cost of the bill. 
bill = input("What was the total bill? ")
# Captures how many patrons there are.
num_of_diners = input("How many people are splitting this bill? ")
# Captures the percentage amount the patrons wich to tip and then converts it to an integer.  
tip_percentage = (int(input("What percentage tip would you like to leave your waiter? ")))/100
# Calculates the total each patron is responsible for with 
calculation = round((float(bill) + ((float(bill) * tip_percentage)))/int(num_of_diners), 2)
#Properly formats the final output of the program.  
final_format = "{:.2f}".format(calculation)

print(f"Each person should pay ${final_format}")



