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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_check(drink_ingredients):
    """Returns True if enough resources to make drink, and False if not."""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def money_handler():
    """Returns the total amount of coins inserted."""
    print("Please insert coins.")
    total_amount = float(input("How many quarters?: ")) * 0.25
    total_amount += float(input("How many dimes?: ")) * 0.10
    total_amount += float(input("How many nickles?: ")) * 0.05
    total_amount += float(input("How many pennies?: ")) * 0.01
    return round(total_amount, 2)


def enough_money(amount_given, drink_cost):
    """Returns True when payment accepted and False if insufficient money."""
    if amount_given >= drink_cost:
        change = round(amount_given - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here's your {drink_name}. Enjoy!")


is_on = True
while is_on:
    drink = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        choice = MENU[drink]
        if resources_check(drink_ingredients=choice["ingredients"]):
            payment = money_handler()
            if enough_money(amount_given=payment, drink_cost=choice["cost"]):
                make_coffee(drink_name=drink, drink_ingredients=choice["ingredients"])
    elif drink == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ${profit}")
    elif drink == "off":
        is_on = False
    else:
        print("Please insert a valid order.")
