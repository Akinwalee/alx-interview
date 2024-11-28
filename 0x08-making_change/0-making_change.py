#!/usr/bin/python3

def makeChange(coins, total):

    if total <= 0:
        return 0

    arr = [float('inf')] * (total + 1)
    arr[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                arr[i] = min(arr[i], arr[i - coin] + 1)

    return arr[total] if arr[total] != float('inf') else -1
