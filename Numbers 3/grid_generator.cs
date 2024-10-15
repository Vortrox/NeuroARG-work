using System;
 
class Program
{
    static void Main()
    {
        char[,] grid = CreateGrid();
 
        Console.WriteLine("Original Grid:");
        PrintGrid(grid);
 
        int[] keyNumbers = { };
        RotateGrid(grid, keyNumbers);
 
        Console.WriteLine("\nEncrypted Grid after Rotating");
        PrintGrid(grid);
    }
 
    static char[,] CreateGrid()
    {
        char[,] grid = new char[6, 6];
        string alphabet = "abcdefghijqlmnopqrstuvwxyz1234567890";
        int index = 0;
 
        for (int row = 0; row < 6; row++)
        {
            for (int col = 0; col < 6; col++)
            {
                grid[row, col] = alphabet[index];
                index++;
            }
        }
 
        return grid;
    }
 
    static void PrintGrid(char[,] grid)
    {
        for (int row = 0; row < 6; row++)
        {
            for (int col = 0; col < 6; col++)
            {
                Console.Write(grid[row, col] + " ");
            }
 
            Console.WriteLine();
        }
    }
 
    static void RotateGrid(char[,] grid, int[] keyNumbers)
    {
        for (int i = 0; i < keyNumbers.Length; i++)
        {
            int rotationAmount = keyNumbers[i];
            if (i < 6) 
            {
                RotateRow(grid, i%6, rotationAmount);
            }
            else
            {
                RotateColumn(grid, (i-6) % 6, rotationAmount);
            }
        }
        
    }
 
    static void RotateRow(char[,] grid, int row, int amount) 
    {
       
        amount %= 6;
        char[] temp = new char[6];
 
        for (int col = 0; col < 6; col++) 
        {
            temp[col] = grid[row, col];
        }
        
        for (int col = 0; col < 6; col++) 
        {
            grid[row, col] = temp[(col - amount + 6) % 6];
        }
    }
    
    static void RotateColumn(char[,] grid, int col, int amount) {
        amount %= 6;
        char[] temp = new char[6];
 
        for (int row = 0; row < 6; row++) {
            temp[row] = grid[row, col];
        }
        for (int row = 0; row < 6; row++) {
            grid[row, col] = temp[(row - amount + 6) % 6];
        }
    }
}