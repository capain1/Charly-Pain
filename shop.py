class NotEnoughMoneyError(Exception):
    pass

items = {
    'Croissant': 50,
    'Brie': 120,
    'Lemon': 75
}

money = 100

def print_items():
    print("Available items:")
    for item, price in items.items():
        print(f"{item}: £{price}")
    print("Exit: To exit the shop")

print("Welcome to the shop!")
print_items()

purchased = False
for i in range(3):
    try:
        choice = input("What would you like to buy? ")
        if choice == "Exit":
            print("Thank you for shopping with us!")
            break
        price = items[choice]
        if money < price:
            raise NotEnoughMoneyError("You don't have enough money for that!")
        else:
            print(f"Here's your {choice}!")
            money -= price
            print(f"You have £{money} left")
            purchased = True
    except KeyError:
        print("Invalid item choice!")
    except NotEnoughMoneyError as e:
        print(e)
        more_money = input("Do you have more money? (Y/N) ")
        if more_money.upper() == "Y":
            additional_money = int(input("Enter amount: "))
            money += additional_money
            print(f"You now have £{money}")
        else:
            print("Thank you for shopping with us!")
            break
    finally:
        if purchased:
            print("Thank you for shopping with us!")
            break
        elif i == 2:
            print("Maximum purchase attempts reached. Thank you for shopping with us!")

input("Press Enter to exit...")