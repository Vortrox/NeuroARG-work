import re


def calculate_fibonacci(x: int) -> int:
    """Calculates the xth term of the fibonacci sequence"""
    prev_num = 1
    current_num = 1
    for i in range(2, x):
        temp = current_num
        current_num += prev_num
        prev_num = temp

    return current_num


lyrics = """
Add another 6 yeah
Flip the numbers backwards
Make the 2 a 3 yeah
Abcdefg
Multiply by 9 yeah
Add the numbers 2 (might be “to”) 4
17 is first yeah
Abcdefg
""".split("\n")[1:-1]

updated_lyrics = []
for line in lyrics:
    updated_line = ""
    numbers_in_line = re.findall("\d+", line)
    for fragment in re.split("\d+", line):
        updated_lyrics.append(line.replace(num, str(calculate_fibonacci(int(num)))))
pass

