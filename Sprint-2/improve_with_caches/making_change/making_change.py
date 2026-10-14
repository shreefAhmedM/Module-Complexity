from typing import List


def ways_to_make_change(total: int) -> int:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache = {}

    def helper(remaining: int, coin_index: int) -> int:
        if remaining == 0:
            return 1

        if remaining < 0 or coin_index == len(coins):
            return 0

        key = (remaining, coin_index)

        if key in cache:
            return cache[key]

        result = (
            helper(remaining - coins[coin_index], coin_index)
            + helper(remaining, coin_index + 1)
        )

        cache[key] = result
        return result

    if total < 0:
        return 0

    return helper(total, 0)


def ways_to_make_change_helper(total: int, coins: List[int]) -> int:
    cache = {}

    def helper(remaining: int, coin_index: int) -> int:
        if remaining == 0:
            return 1

        if remaining < 0 or coin_index == len(coins):
            return 0

        key = (remaining, coin_index)

        if key in cache:
            return cache[key]

        result = (
            helper(remaining - coins[coin_index], coin_index)
            + helper(remaining, coin_index + 1)
        )

        cache[key] = result
        return result



    if total < 0:
        return 0

    return helper(total, 0)