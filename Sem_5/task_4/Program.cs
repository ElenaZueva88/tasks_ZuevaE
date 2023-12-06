/* Задача 4*(не обязательная): Задайте двумерный массив из целых чисел. 
Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.
 Под удалением понимается создание нового двумерного массива без строки и столбца */

static int[,] CreateArray(int row, int col, int min, int max)
{
    int[,] array = new int[row, col];
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                array[i, j] = new Random().Next(min, max + 1);
            }
        }
    return array;
}

static void ShowArray(int[,] array)
{
        for (int i = 0; i < array.GetLength(0); i++)
        {
            for (int j = 0; j < array.GetLength(1); j++)
            {
                Console.Write(array[i, j] + " ");
            }
                Console.WriteLine();
        }
}