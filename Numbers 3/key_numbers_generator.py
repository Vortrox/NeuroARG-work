from itertools import product
from typing import Iterable


def generate_key_numbers(initial_numbers: list[int], length: int=12) -> Iterable[tuple[int]]:
    # Increases the chance of same key numbers being generated and filtered
    numbers = [n % 6 for n in initial_numbers]

    numbers = numbers + [0] * (length - len(numbers))
    # todo: Handle case where there are more initial numbers than the length. In that case return permutations of adding
    #  each extra numbers to each other until at the length limit

    # todo: If we could generate the key numbers without duplicates in the first place, that would be better than
    #  filtering them as they're generated as it will greatly reduce memory usage
    # Potentially high memory usage, upper bound is exponential O(2^n)
    seen_key_numbers = set()
    for p in product(numbers, repeat=length):
        if p not in seen_key_numbers:
            seen_key_numbers.add(p)
            yield p

if __name__ == "__main__":
    for p in generate_key_numbers(list(range(6))):
        print(p)
