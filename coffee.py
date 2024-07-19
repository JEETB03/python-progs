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


print("""( (
    ) )
  ........
  |      |]
  \      /    
   `----'""")


def is_sufficient_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True
    

def payment_processing():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def check_transaction(money_received, drink_cost):
    """Returns the change owed."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def make_coffee(coffee_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}☕. Enjoy and have a nice day!")



machine_is_on = True


while machine_is_on:
    """When Coffee Machine is started and customer is prompted with options."""
    coffee_choice = input("""What would you like? (Espresso / Latte / Cappuccino): 
    To Check ingredients (Report):  
    To Turn off the machine (Off): """).lower()
    if coffee_choice == "off":
        machine_is_on = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee_choice]
        if is_sufficient_resources(drink["ingredients"]):
            payment = payment_processing()
            if check_transaction(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])



