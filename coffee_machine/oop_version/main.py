from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_menu = Menu()

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

is_on = True
while is_on:
    # ask consumer to select coffee
    coffee = input(f"What would you like? ({my_menu.get_items()}): ")

    if coffee == "off":
        is_on = False
    elif coffee == "report": # note using elif here is much cleaner than using while
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_drink = my_menu.find_drink(coffee)  #find_drink method returns a MenuItem object
        if my_drink is not None:
            #note the function can print and return eventho it is in if statement.
            if my_coffee_maker.is_resource_sufficient(my_drink):
                if my_money_machine.make_payment(my_drink.cost):
                    my_coffee_maker.make_coffee(my_drink)






