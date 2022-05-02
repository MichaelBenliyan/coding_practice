from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
machine_running = True
while machine_running == True: 
    user_input = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if user_input == "off":
        machine_running = False 
    elif user_input == "report":
        my_coffee_maker.report()
        my_coffee_maker.report()
    else: 
        drink = my_menu.find_drink(user_input)
        if drink != None:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
        
