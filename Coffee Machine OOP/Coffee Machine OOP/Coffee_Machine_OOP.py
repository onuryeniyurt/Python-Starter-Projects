from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

machine_on=True

while machine_on:
    ans=input(f"What would you like to have? {menu.get_items()}")
    
    if ans=="off":
        machine_on=False
    elif ans=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(ans)
        is_possible=coffee_maker.is_resource_sufficient(drink)
        if is_possible:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    
