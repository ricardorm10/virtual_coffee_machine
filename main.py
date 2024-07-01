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


def profit_calculation(current_profit, type_of_drink):
    """Take the amount of money as input, and """
    quarter_qty = float(input("How many quarters?: "))
    dimes_qty = float(input("How many dimes?: "))
    nickles_qty = float(input("How many nickles?: "))
    pennies_qty = float(input("How many pennies?: "))

    # Amount calculation.
    total_quarters = 0.25 * quarter_qty
    total_dimes = 0.10 * dimes_qty
    total_nickles = 0.05 * nickles_qty
    total_pennies = 0.01 * pennies_qty
    total_amount = total_quarters + total_dimes + total_nickles + total_pennies

    if MENU[type_of_drink]["cost"] < total_amount:
        client_change = round(total_amount - MENU[type_of_drink]["cost"], 2)
        print(f"Here is ${client_change} in change.")
        print(f"Here is your {type_of_drink}. Enjoy!")
        return current_profit + MENU[type_of_drink]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded")
        return current_profit


# TODO 1: Fix resource consumption function.
# TODO 2: Profit handling.
# TODO 3: Create a function to see if the amount of resources is enough to prepare a coffee.


def resource_consumption(order_resource_consumption):
    """Takes into account the current resources and determines if they are enough to make a certain coffee."""
    if order_resource_consumption == "latte" or order_resource_consumption == "cappuccino":
        resources["water"] -= MENU[order_resource_consumption]["ingredients"]["water"]
        resources["coffee"] -= MENU[order_resource_consumption]["ingredients"]["coffee"]
        resources["milk"] -= MENU[order_resource_consumption]["ingredients"]["milk"]
    else:
        resources["water"] -= MENU[order_resource_consumption]["ingredients"]["water"]
        resources["coffee"] -= MENU[order_resource_consumption]["ingredients"]["coffee"]


is_on = True
while is_on:
    order = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        print("Please insert coins.")
        profit_calculation(current_profit=profit, type_of_drink=order)
    elif order == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ${profit}")
    elif order == "off":
        is_on = False
    else:
        print("Please insert a valid order.")
