MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

#function that takes money and return change.

def payment():
    coins = ['quarters', 'nickles','dimes','pennies']
    coin_value = [.25, .05, .10, .01]
    user_paid = []
    count = 0
    while count < 4:
        num_of_coins = int(input(f"How many {coins[count]}?"))
        user_paid.append(num_of_coins * coin_value[count])
        count += 1
    return sum(user_paid)


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





off = False


while not off:
    order = input("What would you like? (espresso/latte/cappucino):")

    if order == 'report':
        for key, value in resources.items():
            print(key, ':', value)

    if order == 'espresso' and resources['water'] >= 50 and resources['coffee'] >= 18:
        amount_paid = payment()
        if amount_paid >= MENU['espresso']['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['espresso']['cost']), 2)}")
            print("Here is your espresso.")
        else:
            print("Money refunded.")
            off = True
    if order == 'latte' and resources['water'] >= 200 and resources['water'] >= 24 and resources['milk'] >= 150:
        amount_paid = payment()
        if amount_paid >= MENU['latte']['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['latte']['cost']), 2)}")
            print('Here is your latte.')
        else:
            print("Money refunded.")
            off = True
    if order == 'cappuccino' and resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:
        amount_paid = payment()
        if amount_paid >= MENU["cappuccino"]['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['cappucino']['cost']), 2)}")
            print("Here is your cappuccino.")
        else:
            print("Money refunded.")
            off = True
   


