# Original: https://pastebin.com/DcSVS7FZ

def main():
    grid = create_grid()

    print("Original Grid:")

    print_grid(grid)

    key_numbers = []
    rotate_grid(grid, key_numbers)

    print("\nEncrypted Grid after Rotating")
    print_grid(grid)

def create_grid() -> list[list[str]]:
    grid = [["" for j in range(6)] for i in range(6)]
    alphabet = "abcdefghijqlmnopqrstuvwxyz1234567890"
    index = 0

    for row in range(6):
        for col in range(6):
            grid[row][col] = alphabet[index]
            index += 1

    return grid

def print_grid(grid: list[list[str]]):
    for row in range(6):
        for col in range(6):
            print(grid[row][col] + " ", end="")

        print()

def rotate_grid(grid: list[list[str]], key_numbers: list[int]):
    for i in range(len(key_numbers)):
        rotation_amount = key_numbers[i]
        if i < 6:
            rotate_row(grid, i % 6, rotation_amount)
        else:
            rotate_column(grid, (i - 6 ) % 6, rotation_amount)

def rotate_row(grid: list[list[str]], row: int, amount: int):
    amount %= 6
    temp = ["" for i in range(6)]

    for col in range(6):
        temp[col] = grid[row][col]

    for col in range(6):
        grid[row][col] = temp[(col - amount + 6) % 6]

def rotate_column(grid: list[list[str]], col: int, amount: int):
    amount %= 6
    temp = ["" for i in range(6)]

    for row in range(6):
        temp[row] = grid[row][col]

    for row in range(6):
        grid[row][col] = temp[(row - amount + 6) % 6]