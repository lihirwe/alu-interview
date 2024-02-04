#!/usr/bin/python3

"""
rain.py

This script defines a function to
calculate the amount of rainwater retained between walls.
"""


def rain(walls):
    """
    Calculate the amount of rainwater retained between walls.
    """
    if not walls:
        return 0
    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])
    total_rainwater = 0
    for i in range(n):
        total_rainwater += min(left_max[i], right_max[i]) - walls[i]
    return total_rainwater
