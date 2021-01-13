from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_cm_running = True

    while is_cm_running:
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

        if user_action == "off":
            is_cm_running = False
            continue
        elif user_action == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            coffee = menu.find_drink(user_action)
            if coffee_maker.is_resource_sufficient(coffee) and \
                    money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)


if __name__ == "__main__":
    main()
