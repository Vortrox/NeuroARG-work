from itertools import product
from typing import Iterable


def numbers_permutations(initial_numbers: list[int], length: int) -> Iterable[tuple[int]]:
    numbers = initial_numbers + [0] * (length - len(initial_numbers))
    # todo: Handle case where there are more initial numbers than the length. In that case return permutations of adding
    #  each extra numbers to each other until at the length limit

    return product(numbers, repeat=length)

if __name__ == "__main__":
    seen = set()
    for p in numbers_permutations(list(range(6)), 12):
        if p not in seen:
            seen.add(p)
            print(p)
