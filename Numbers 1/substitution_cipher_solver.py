import string

mappings = {}


def map_letters(sequence_from: str, sequence_to: str, input_mappings=None):
    if input_mappings is None:
        input_mappings = mappings

    if len(sequence_from) != len(sequence_to):
        raise ValueError("Both sequences must have the same length")

    sequence_from = sequence_from.lower()
    sequence_to = sequence_to.lower()

    for i, _ in enumerate(sequence_from):
        input_mappings[sequence_from[i]] = sequence_to[i]


def print_with_mappings(sequence: str, input_mappings=None, default_char: str = None):
    if input_mappings is None:
        input_mappings = mappings

    output = ""
    for c in sequence:
        if c in input_mappings.keys():
            output += input_mappings[c]
        elif default_char is not None and c not in {" ", "'"}:
            output += default_char
        else:
            output += c

    print(output)


s1 = "C iegj ptqv din jlx btdqokwv cn, vr'c eedbh, hti uxrd, lpu zpxb pcz cjfpokr rpws zudry."

s1 = s1.lower()

# map_letters("vr'c", "it's")
map_letters("btdqokwv", "involved")

char_to_num = {c: i for i, c in enumerate(string.ascii_lowercase)}

results = []
for i in range(26):
    c = string.ascii_lowercase[i]
    if c in mappings.keys():
        results.append((f"{c} -> {mappings[c]}", (char_to_num[c] - char_to_num[mappings[c]]) % 26))

print(results)
print_with_mappings(s1, default_char="_")
pass
