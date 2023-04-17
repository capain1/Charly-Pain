
# coins customer has 2 x £2.00  6 x £1.00 10 x £0.50  4 x £0.20  6 x £0.10  7 x £0.05 4 x £0.02  6 x £0.01
# Need to  to return the smallest amount of coins
#

def calculate_coins(cost):
    # create a dictionary containing the coin value and the number of each coins
    coins = {2.00: 2, 1.00: 6, 0.50: 10, 0.20: 4, 0.10: 6, 0.05: 7, 0.02: 4, 0.01: 6}

    # create a dictionary containing the coin value and the number of each coins used
    coins_used = {2.00: 0, 1.00: 0, 0.50: 0, 0.20: 0, 0.10: 0, 0.05: 0, 0.02: 0, 0.01: 0}

    # if the customer cant afford it give the message
    if cost > sum(coins.values()):
        return "Can't afford this with the available petty change"

    for coin in coins:
        # while the cost is greater than the current coin value and there are still coins of that value available
        while cost >= coin and coins[coin] > 0:

            cost -= coin # subtract the value of the coin from the cost
            coins[coin] -= 1 # go down in list of the coins of that value available
            coins_used[coin] += 1 # go up the the number of coins of that value used
    return coins_used

Cost = calculate_coins(16.89)
print(Cost)

