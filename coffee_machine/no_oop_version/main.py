def print_report(water, milk, coffee, money):
    print(f"""
Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: ${money}
          """)
def main():
    # initiate resources
    from menu import resources, MENU
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    money_amount = 0

    is_on = True
    while is_on:
        # ask consumer to select coffee
        coffee = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee == "off":
            is_on = False
        elif coffee == "report": # note using elif here is much cleaner than using while
            print_report(water_amount, milk_amount, coffee_amount, money_amount)
        else:
            water_needed = MENU[coffee]['ingredients']['water']
            milk_needed = MENU[coffee]['ingredients']['milk']
            coffee_needed = MENU[coffee]['ingredients']['coffee']
            money_needed = MENU[coffee]['cost']

            if water_needed > water_amount:
                print("Sorry there is not enough water.")
            elif milk_needed > milk_amount:
                print("Sorry there is not enough milk.")
            elif coffee_needed > coffee_amount:
                print("Sorry there is not enough coffee.")
            else:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                money_insert = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

                if money_insert < money_needed:
                    print("Sorry that's not enough money. Money refunded")
                else:
                    water_amount -= water_needed
                    milk_amount -= milk_needed
                    coffee_amount -= coffee_needed
                    money_amount += money_needed
                    money_refund = money_insert - money_needed
                    print(f"Here is {money_refund} in change.")
                    print(f"Here is your {coffee}. Please enjoy!")

if __name__ == '__main__':
    main()
