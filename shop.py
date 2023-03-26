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


def purchase_item(choice):
    global money
    global purchased

    try:
        price = items[choice]  # Raises KeyError if choice is not in items
        if money < price:
            raise NotEnoughMoneyError("You don't have enough money for that!")
        else:
            print(f"Here's your {choice}!")
            money -= price
            print(f"You have £{money} left")
            purchased = True
    except NotEnoughMoneyError as e:
        print(e)
        more_money = input("Do you have more money? (Y/N) ")
        if more_money.upper() == "Y":
            additional_money = int(input("Enter amount: "))
            money += additional_money
            print(f"You now have £{money}")
        else:
            print("Thank you for shopping with us!")
            purchased = False
    except KeyError:
        print("Invalid item choice!")
        purchased = False


print("Welcome to the shop!")
print_items()

purchased = False
for i in range(3):
    choice = input("What would you like to buy? ")
    if choice == "Exit":
        print("Thank you for shopping with us!")
        break
    else:
        purchase_item(choice)

    if purchased:
        print("Thank you for shopping with us!")
        break
    elif i == 2:
        raise KeyError("Maximum purchase attempts reached. Thank you for shopping with us!")

input("Press Enter to exit...")