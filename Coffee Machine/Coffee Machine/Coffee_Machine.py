MENU={
    "espresso":{"ingredients":{"water":50,"milk":0,"coffee":18},"cost":1.5},
    "latte":{"ingredients":{"water":200,"milk":150,"coffee":24},"cost":2.5},
    "cappuccino":{"ingredients":{"water":250,"milk":100,"coffee":24},"cost":3.0}
    }

resources={"water":300,"milk":200,"coffee":100}

def control(_item):
    for i in resources:
        if resources[i]>=_item[i]:
            return True
        else:
            return False



def coffee_machine():
    global resources
    machine_off=False
    while not machine_off:
        ans=input("Would you like to have espresso/latte/cappuccino?").lower()
    
        if ans=="report":
            print(f"Water: {resources["water"]}")
            print(f"Milk: {resources["milk"]}")
            print(f"Coffee: {resources["coffee"]}")
        
        elif ans=="off":
            print("Coffee machine is turning off...")
            machine_off=True
        
        else:
            quarters=float(input("Quarters:"))
            dimes=float(input("Dimes: "))
            nickles=float(input("Nickles: "))
            pennies=float(input("Pennies: "))
        
            money=(quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
            
            
            if control(MENU[ans]["ingredients"]):
        
                if money==MENU[ans]["cost"]:
                    
                    print(f"Here is your {ans}")
                    resources["water"] -=MENU[ans]["ingredients"]["water"]
                    resources["milk"] -=MENU[ans]["ingredients"]["milk"]
                    resources["coffee"] -=MENU[ans]["ingredients"]["coffee"]
            
                elif money>MENU[ans]["cost"]:
                    
                    print(f"Here is your {ans} and your {money-MENU[ans]["cost"]} change.")
                    resources["water"] -=MENU[ans]["ingredients"]["water"]
                    resources["milk"] -=MENU[ans]["ingredients"]["milk"]
                    resources["coffee"] -=MENU[ans]["ingredients"]["coffee"]
            else:
                print("Sorry not enough resources... Money is returning.")
                machine_off=True
            


coffee_machine()
        