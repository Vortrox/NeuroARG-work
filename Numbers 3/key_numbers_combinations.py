from itertools import permutations
from typing import Iterable


def numbers_permutations(initial_numbers: list[int], length: int) -> Iterable[tuple[int]]:
    numbers = initial_numbers + [0] * (length - len(initial_numbers))

    return permutations(numbers, length)

if __name__ == "__main__":
    seen = set()
    for p in numbers_permutations(list(range(6)), 12):
        if p not in seen:
            seen.add(p)
            print(p)
