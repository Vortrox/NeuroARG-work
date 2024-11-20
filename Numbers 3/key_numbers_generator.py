from itertools import permutations, product
from typing import Iterable


def generate_keys(key_length: int=12, unfixed_numbers: list[int]=None, fixed_numbers: list[int]=None, repeatable_numbers: list[int]=None) -> Iterable[tuple[int]]:
    """
    A key consists of up to 12 numbers of integers 0-5. The first 6 numbers specifies the number of times to rotate each
    row of the 6x6 grid while the last 6 numbers specifies the number of times to rotate each column of the 6x6 grid.
    This function returns an iterable that yields possible keys for rotating the grid. There can be up to 6^12 possible
    keys. The quantity of keys searched can be greatly reduced by:
    - Reducing key length
    - Increasing number of unfixed numbers
    - Increasing number of fixed numbers
    - Reducing number of unfixed repeatable numbers

    :param key_length: The length of each key (max 12). If less than 12, not all rows/columns will be rotated.
    :param unfixed_numbers: List of numbers to place anywhere in the key exactly once for each instance of each number
    :param fixed_numbers: List of integers defining where specific numbers should be placed. Use -1 to specify
    positions that can be filled with any number. Must be the same size as key length. Example: [-1, -1, -1, 0, 3, -1]
    :param repeatable_numbers: List of numbers to place anywhere in the key as many times as necessary to fill the key
    to the desired length
    :return: Iterable of possible keys matching the specifications
    """
    if unfixed_numbers is None:
        unfixed_numbers = []
    if repeatable_numbers is None:
        repeatable_numbers = [0, 1, 2, 3, 4, 5]
    if fixed_numbers is None:
        fixed_numbers = [-1] * 12

    if len(fixed_numbers) != key_length:
        raise ValueError(f"Number of fixed numbers ({len(fixed_numbers)}) != key length ({key_length})")
    if len(unfixed_numbers) < key_length and len(repeatable_numbers) == 0:
        raise ValueError(f"At least 1 repeatable number is required if the number of unfixed numbers "
                         f"({len(unfixed_numbers)}) is less than key length ({key_length})")

    # todo: Are all of these features really necessary? Consider generating all 6^12 keys, using them on the 6x6 grid
    #  and checking the resulting grid for validity instead.
    # Rotating each row/column 5 times will loop it back to its original state thus doing so is pointless. Constraining
    # input numbers to 0-5 increases the chance of same key numbers being generated and filtered. 0s act as a no-op.
    unfixed_numbers = list(set(n % 6 for n in unfixed_numbers))
    repeatable_numbers = list(set(n % 6 for n in repeatable_numbers))
    fixed_numbers = [n if n == -1 else n % 6 for n in fixed_numbers]

    # todo: Handle case where there are more unfixed numbers than the key length. In that case return permutations of
    #  adding each extra numbers to each other until at the desired length. Useful in situations where other ARG
    #  participants suggest a set of numbers longer than 12 as the key numbers.

    key_length -= len(fixed_numbers) - fixed_numbers.count(-1)

    # todo: Reduce memory usage by generating key numbers without duplicates instead of filtering out duplicates
    def h() -> Iterable[tuple[int]]:
        # Potentially high memory usage, upper bound is exponential O(2^n)
        seen_key_numbers = set()
        def number_permutations(numbers: list[int]):
            for p in permutations(numbers, key_length):
                if p not in seen_key_numbers:
                    seen_key_numbers.add(p)
                    yield p

        n_repeatable_numbers = key_length - len(unfixed_numbers)
        if n_repeatable_numbers <= 0:
            return number_permutations(unfixed_numbers)

        for repeatable_numbers_product in product(repeatable_numbers, repeat=n_repeatable_numbers):
            for perm in number_permutations(unfixed_numbers + list(repeatable_numbers_product)):
                yield perm

    # Replace -1s in fixed_numbers with possible permutations from unfixed_numbers and repeatable_numbers to create
    # possible keys
    replaceable_numbers_mask = [i for i, n in enumerate(fixed_numbers) if n != -1]
    for nums in h():
        key_number = repeatable_numbers.copy()
        for i, n in zip(replaceable_numbers_mask, nums):
            key_number[i] = n
        yield key_number


if __name__ == "__main__":
    for p in generate_keys(key_length=5, unfixed_numbers=list(range(2)), repeatable_numbers=[2, 3]):
        print(p)
