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

def make_drink(type_of_drink):
    if type_of_drink == 'espresso':
        resources['water'] = resources['water'] - 50
        resources["coffee"] = resources['coffee'] - 18
    if type_of_drink == 'latte':
        resources["water"] = resources["water"] - 200
        resources["milk"] = resources["milk"] - 150
        resources['coffee'] = resources['coffee'] - 24
    if type_of_drink == 'cappuccino':
        resources['water'] = resources["water"] - 250
        resources['milk'] = resources['milk'] - 100
        resources["coffee"] = resources['coffee'] - 24
    return resources




off = False


while not off:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()

    if order == 'report':
        for key, value in resources.items():
            print(key, ':', value)

    if order == 'espresso' and resources['water'] >= 50 and resources['coffee'] >= 18:
        amount_paid = payment()
        if amount_paid >= MENU['espresso']['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['espresso']['cost']), 2)}")
            new_resources = make_drink(order)
            print("Here is your espresso.")
        if amount_paid < MENU['espresso']['cost']:
            print("Money refunded.")
        if resources['water'] < 50 or resources['coffee'] < 18:
            print("out of ingredients for espresso please turn off machine to restock.")
    if order == 'latte' and resources['water'] >= 200 and resources['water'] >= 24 and resources['milk'] >= 150:
        amount_paid = payment()
        if amount_paid >= MENU['latte']['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['latte']['cost']), 2)}")
            new_resources = make_drink(order)
            print('Here is your latte.')
        if amount_paid < MENU['latte']['cost']:
            print("Money refunded.")
        if resources['water'] < 200 or resources['water'] < 24 or resources['milk'] < 150:
            print("out of ingredients latte please turn off machine to restock.")
    if order == 'cappuccino' and resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:
        amount_paid = payment()
        if amount_paid >= MENU["cappuccino"]['cost']:
            print(f"Here is your change, ${round(amount_paid - (MENU['cappuccino']['cost']), 2)}")
            new_resources = make_drink(order)
            print("Here is your cappuccino.")
        if amount_paid < MENU['cappuccino']['cost']:
            print("Money refunded.")
        if resources['water'] < 250 or resources['coffee'] < 24 or resources['milk'] < 100:
            print("out of ingredients for cappuccino please turn off machine to restock.")
    if order == 'off':
        off = True
   


