static char[,] Swap(char[,] grid, int row_a, int col_a, int row_b, int col_b)
{
    temp = grid[row_a, col_a]
    grid[row_a, col_a] = grid[row_b, col_b]
    grid[row_b, col_b] = temp
}

static char[,] FlipVertical(char[,] grid)
{
    for (int row = 0; row < 6; row++)
    {
        Swap(grid, row, 0, row, 5)
        Swap(grid, row, 1, row, 4)
        Swap(grid, row, 2, row, 3)
    }
}
