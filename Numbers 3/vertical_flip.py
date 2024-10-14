def swap(grid: list[list[str]], row_a: int, col_a: int, row_b: int, col_b: int):
    temp = grid[row_a][col_a]
    grid[row_a][col_a] = grid[row_b][col_b]
    grid[row_b][col_b] = temp


def flip_vertical(grid: list[list[str]]):
    for row in range(6):
        swap(grid, row, 0, row, 5)
        swap(grid, row, 1, row, 4)
        swap(grid, row, 2, row, 3)