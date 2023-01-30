MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#function that takes money and return change.

def payment():
    coins = ['quarters', 'nickles','dimes','pennies']
    coin_value = [.25, .05, .10, .01]
    user_paid = []
    count = 0
    for _ in range(len(coins)):
        num_of_coins = int(input(f"How many {coins[count]}?"))
        user_paid.append(num_of_coins * coin_value[count])
        count += 1
    print(sum(coin_value))


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Function that takes user inputs
order = input("What would you like? (espresso/latte/cappucino):")

if order == 'report':
    for key, value in resources.items():
        print(key, ':', value)

if order == 'espresso' and resources['water'] >= 50 and resources['coffee'] >= 18:
    payment()


