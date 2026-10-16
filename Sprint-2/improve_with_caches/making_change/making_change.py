
from typing import List

# Define coin values globally
COIN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(total: int) -> int:
    """
    Given coin values of 1, 2, 5, 10, 20, 50, 100, and 200,
    return the number of ways to make the given total.
    """
    memo = {}
    return change_helper(total, 0, memo)


def change_helper(amount: int, index: int, memo: dict) -> int:
    """Helper function to calculate the number of ways."""

    key = (amount, index)

    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if index >= len(COIN_VALUES):
        return 0

    result = 0

    for position in range(index, len(COIN_VALUES)):
        value = COIN_VALUES[position]
        quantity = 1

        while value * quantity <= amount:
            current_sum = value * quantity

            if current_sum == amount:
                result += 1
            else:
                remaining = change_helper(
                    amount - current_sum,
                    position + 1,
                    memo
                )
                result += remaining

            quantity += 1

    memo[key] = result
    return result
