
from typing import List


def find_longest_common_prefix(strings: List[str]) -> str:
    """
    Return the longest common prefix shared by any two strings.
    Return an empty string if fewer than two strings are provided
    or no non-empty common prefix exists.
    """
    if len(strings) < 2:
        return ""

    # Precompute the sorted order to avoid comparing every pair
    ordered_strings = sorted(strings)

    longest = ""

    for index in range(len(ordered_strings) - 1):
        common = find_common_prefix(
            ordered_strings[index],
            ordered_strings[index + 1]
        )

        if len(common) > len(longest):
            longest = common

    return longest


def find_common_prefix(left: str, right: str) -> str:
    limit = min(len(left), len(right))

    for index in range(limit):
        if left[index] != right[index]:
            return left[:index]

    return left[:limit]
