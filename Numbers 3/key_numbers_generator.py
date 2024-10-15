from itertools import permutations, product
from typing import Iterable


def generate_key_numbers(initial_numbers: list[int], length: int=12, filler_numbers: Iterable=None) -> Iterable[tuple[int]]:
    if filler_numbers is None:
        filler_numbers = [0]
    # Increases the chance of same key numbers being generated and filtered
    initial_numbers = [n % 6 for n in initial_numbers]

    # todo: Handle case where there are more initial numbers than the length. In that case return permutations of adding
    #  each extra numbers to each other until at the length limit

    # todo: If we could generate the key numbers without duplicates in the first place, that would be better than
    #  filtering them as they're generated as it will greatly reduce memory usage
    # Potentially high memory usage, upper bound is exponential O(2^n)
    seen_key_numbers = set()
    def number_permutations(numbers: list[int]):
        for p in permutations(numbers, length):
            if p not in seen_key_numbers:
                seen_key_numbers.add(p)
                yield p

    n_filler_numbers = length - len(initial_numbers)
    if n_filler_numbers <= 0:
        return number_permutations(initial_numbers)

    for filler in product(filler_numbers, repeat=n_filler_numbers):
        for perm in number_permutations(initial_numbers + list(filler)):
            yield perm


if __name__ == "__main__":
    for p in generate_key_numbers(list(range(2)), length=5, filler_numbers=[2, 3]):
        print(p)
