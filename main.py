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
    "money": 0.0
}

print("\n---[Welcome to the state of the art coffee machine]---")
print("\n**Type 'report' to get a report of the resources available**")
print("**Type 'off' or 'exit' to turn off machine and exit the program**")


def check_resources(coffee):
    for key in (resources and MENU[coffee]["ingredients"]):
        if resources[key] >= MENU[coffee]["ingredients"][key]:
            print(f"\nenough resources available for {coffee}")
            print(f"{coffee} costs ${MENU[coffee]['cost']}\n")
            return True
        else:
            print(f"\nSorry, not enough resources available for {coffee}")
            return False


def adjust_resources(coffee):
    # reducing resources
    for key in (resources and MENU[coffee]["ingredients"]):
        resources[key] -= MENU[coffee]["ingredients"][key]

    # adding money to resources:
    resources["money"] += MENU[coffee]["cost"]


def process_coins(coffee):
    num_of_quarters = int(input("How many quarters? "))
    num_of_dimes = int(input("How many dimes? "))
    num_of_nickles = int(input("How many nickles? "))
    num_of_pennies = int(input("How many pennies? "))

    cost_of_coffee = MENU[coffee]["cost"]

    user_paid = (0.25 * num_of_quarters) + (0.10 * num_of_dimes) + \
        (0.05 * num_of_nickles) + (0.01 * num_of_pennies)
    print(f"\nyou paid: {user_paid}")

    change = round((user_paid - cost_of_coffee), 2)

    if user_paid == cost_of_coffee:
        print(f"here's your {coffee}, enjoy!\n")

    elif user_paid > cost_of_coffee:
        print(
            f"\nhere's your {coffee} along with your change: ${change} \nenjoy!")

    elif user_paid < cost_of_coffee:
        print(
            f"\nNot enough money for {coffee}, money refunded: ${user_paid}")
        return


def coffee_machine():
    while True:
        user_choice = input(
            "\n\nWhat would you like? [espresso / latte / cappuccino]: ").lower()

        if user_choice == "off" or user_choice == "exit":
            print("\nturning off coffee machine, goodbye!")
            break

        elif user_choice == "report":
            for key in resources:
                if key == "water":
                    print(f"{key}: {resources[key]}ml")
                if key == "milk":
                    print(f"{key}: {resources[key]}ml")
                if key == "coffee":
                    print(f"{key}: {resources[key]}g")
                if key == "money":
                    print(f"{key}: ${resources[key]}")

        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            if check_resources(user_choice):
                process_coins(user_choice)
                adjust_resources(user_choice)
                continue
            else:
                continue


coffee_machine()
