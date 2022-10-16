MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.00

is_machine_on = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    print()


def get_choice():
    return str.lower(input(f"What would you like? (Espresso/Latte/Cappuccino) or type 'report' to browse report.\n"))


def get_coffee_price(coffee):
    return float(MENU[coffee]["cost"])


def print_paid_status(coffee_price, paid):
    if paid > coffee_price:
        print(f"Here is ${format(coffee_price, '.2f')} in change. ${format(paid - coffee_price, '.2f')} refunded.")
    elif paid == coffee_price:
        print(f"Here is ${format(paid, '.2f')} in change.")
    else:
        print(f"You paid ${format(paid, '.2f')}. You need to pay ${format(coffee_price - paid, '.2f')} more.")


def is_paid_enough(coffee):
    is_enough = True
    coffee_price = get_coffee_price(coffee)
    print(f"Please insert coins. A cup of {coffee.capitalize()} is ${coffee_price}")
    paid = 0
    paid += int(input("How many quarters ($0.25)?: ")) * 0.25
    print_paid_status(coffee_price, paid)
    if coffee_price > paid:
        paid += int(input("How many dimes ($0.10)?: ")) * 0.1
        print_paid_status(coffee_price, paid)
        if coffee_price > paid:
            paid += int(input("How many nickles ($0.05)?: ")) * 0.05
            print_paid_status(coffee_price, paid)
            if coffee_price > paid:
                paid += int(input("How many pennies ($0.01)?: ")) * 0.01
                print_paid_status(coffee_price, paid)
                if coffee_price > paid:
                    print(f"Sorry that's not enough money. ${paid} refunded.")
                    print()
                    is_enough = False

    return is_enough


def consume_resources(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def is_resources_sufficient(coffee):
    is_enough = True
    ingredients = MENU[coffee]["ingredients"]
    for ingredient_key in ingredients:
        if resources[ingredient_key] < ingredients[ingredient_key]:
            print(f"Sorry there is not enough {ingredient_key}.")
            print()
            is_enough = False

    return is_enough


def make_coffee(coffee):
    if is_resources_sufficient(coffee):
        if is_paid_enough(coffee):
            consume_resources(coffee)
            print(f"Here is your latte ☕️. Enjoy!")
            print()
            global profit
            profit += get_coffee_price(coffee)


def run_machine():
    choice = get_choice()
    match choice:
        case "espresso":
            make_coffee(choice)
        case "latte":
            make_coffee(choice)
        case "cappuccino":
            make_coffee(choice)
        case "report":
            print_report()
        case "off":
            global is_machine_on
            is_machine_on = False
            print("Machine is turned off for maintenance.")
        case _:
            print("Please type 'espresso', 'latte', 'cappuccino' to order a coffee, or type 'report' to browse report.")


while is_machine_on:
    run_machine()
