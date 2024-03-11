#!/usr/bin/python3
"""
Define makeChange function.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.
    """
    if len(coins) == 0:
        return (-1)

    if total < 1:
        return 0

    coins.sort(reverse=True)

    total_coin = 0
    change = 0
    i = 0

    while change <= total:
        coin = coins[i]
        total_coin += 1
        change += coin

        if change > total:
            change -= coin
            total_coin -= 1
            i += 1

            if i >= len(coins):
                return -1

        if change == total:
            break

    return total_coin
