#!/usr/bin/python3
"""0-making_changes.py """


def makeChange(coins, total):
    """ a function determine the fewest number of coins needed
    to meet a given amount total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
