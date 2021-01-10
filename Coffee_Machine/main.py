from data import MENU, resources


def report(money):
    """Print report of coffee machine resource status"""
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}
    """)


def make_coffee(order):
    """Subtracts resources according to menu for coffee. returns true if successful,
    false if not"""
    ingredients = MENU[order]["ingredients"]

    if order == "espresso" and \
        (resources["water"] - ingredients["water"] < 0 or
            resources["coffee"] - ingredients["coffee"] < 0):
        return False
    elif (order == "latte" or order == "cappuccino") and \
        (resources["water"] - ingredients["water"] < 0 or
         resources["milk"] - ingredients["milk"] < 0 or
            resources["coffee"] - ingredients["coffee"] < 0):
        return False
    else:
        return True


def take_money():
    """Prompts user for money input and puts it into current intake"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


def subtract_resources(order):
    """Subtracts the used ingredients of current order from resources."""
    ingredients = MENU[order]["ingredients"]
    if order == "espresso":
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]
    elif order == "latte" or "cappuccino":
        resources["water"] -= ingredients["water"]
        resources["milk"] -= ingredients["milk"]
        resources["coffee"] -= ingredients["coffee"]


def print_insufficient_resources(order):
    """Prints a list of the insufficient resources"""
    insufficient_resources = []
    ingredients = MENU[order]["ingredients"]
    if resources["water"] - ingredients["water"] < 0:
        insufficient_resources.append("Water")
    if resources["milk"] - ingredients["milk"] < 0:
        insufficient_resources.append("Milk")
    if resources["coffee"] - ingredients["coffee"] < 0:
        insufficient_resources.append("coffee")

    print(f"Sorry there is not enough {insufficient_resources}.")


def main():
    # global variables
    is_coffee_machine_running = True
    money = 0.0

    while is_coffee_machine_running:
        current_money_intake = 0.0

        # ask for user Input
        is_input_invalid = True
        while is_input_invalid:
            user_action = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if user_action == "espresso" or \
                user_action == "latte" or \
                user_action == "cappuccino" or \
                user_action == "report" or \
                    user_action == "off":
                is_input_invalid = False
            else:
                print("Invalid input!")

        # process input
        if user_action == "espresso" or user_action == "latte" or user_action == "cappuccino":
            coffee = make_coffee(user_action)
        elif user_action == "report":
            report(money)
            continue
        elif user_action == "off":
            is_coffee_machine_running = False
            continue

        # check if resources are sufficient
        if coffee:
            # ask for coin
            current_money_intake = take_money()

            # check if enough money was given
            if MENU[user_action]["cost"] > current_money_intake:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif MENU[user_action]["cost"] <= current_money_intake:
                change = current_money_intake - MENU[user_action]["cost"]
                money += MENU[user_action]["cost"]
                if change > 0:
                    print(f"Here is {round(change, 2)} in change.")

                print(f"Here is your {user_action} c(w) Enjoy!")

                subtract_resources(user_action)

        else:
            print_insufficient_resources(user_action)


if __name__ == '__main__':
    main()
