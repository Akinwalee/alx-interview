#!/usr/bin/python3
"""
Determine the winner in a Prime number Game
"""


def isWinner(x, nums):
    """
    Return the winner
    """
    score = [0, 0]
    for num in nums:
        n = getPrimes(num)

        if n % 2:
            score[0] += 1
        else:
            score[1] += 1

    if score[0] > score[1]:
        return "Maria"
    elif score[1] > score[0]:
        return "Ben"

    return None


def getPrimes(num: int) -> int:
    """
    Get the number of prime number between 1 and num
    """

    primes = [True for i in range(num + 1)]
    primes[0] = primes[1] = False

    for p in range(2, int(num ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False

    return sum(primes)
