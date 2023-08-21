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
money_in = 0
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"coffee: {resources['coffee']} g")
    print(f"Money: ${profit}")


def resource_check(drink):
    if drink == "espresso":
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry not enough water")
            return False
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry not enough coffee")
            return False
        else:
            return True
    else:
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry not enough water")
            return False
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry not enough coffee")
            return False
        elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry not enough milk")
            return False
        else:
            return True


def process_coins():
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    money_in = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return money_in


def transaction_check(money_in, drink, profit):
    if money_in < MENU[drink]["cost"]:
        print("Sorry not enough money")
        return False
    else:
        profit += MENU[drink]["cost"]
        print(f"Transaction successful. Here is your ${money_in - MENU[drink]['cost']} in change.")
        return True


def make_coffee(drink):
    print(f"Here is your {drink}. Enjoy!")


machine_on = True

while machine_on:
    order = input("What would you like?")
    if order == "report":
        make_report()
    elif order == "turn off":
        machine_on = False
    else:
        if resource_check(order):
            process_coins()
            if transaction_check(money_in, order, profit):
                make_coffee(order)
