
def count_letters(s: str) -> int:
    """
    Returns the number of letters which only occur in upper case
    in the passed string.
    """
    letters_present = set(s)
    only_upper = set()

    for letter in letters_present:
        if is_upper_case(letter) and letter.lower() not in letters_present:
            only_upper.add(letter)

    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()