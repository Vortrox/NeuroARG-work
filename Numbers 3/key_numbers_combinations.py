def combinations(initial_numbers: list[int], length: int) -> list[list[int]]:
    def h(combination: list[int], remaining_numbers: list[int]):
        if len(combination) == length:
            yield combination

        seen_combos = set()

        for i, number in enumerate(remaining_numbers):
            remaining_numbers_excluding_chosen_number = remaining_numbers[0:i] + remaining_numbers[i+1:len(remaining_numbers)]
            partial_combination = combination + [number]

            # Prevents duplicated combinations
            if tuple(partial_combination) in seen_combos:
                continue
            seen_combos.add(tuple(partial_combination))

            for combo in h(partial_combination, remaining_numbers_excluding_chosen_number):
                yield combo

    number_choices = initial_numbers + [0] * (length - len(initial_numbers))
    combos = [c for c in h([], number_choices)]

    return combos

if __name__ == "__main__":
    print(*combinations([1, 2, 3], 5), sep="\n")
