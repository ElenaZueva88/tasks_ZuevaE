// Задача 2: Задайте массив на 10 целых чисел.
// Напишите программу, которая определяет количество чётных чисел в массиве.


int[] array = new int[10]; 
    Random nums = new Random();

    for (int i = 0; i < array.Length; i++)    //
    {                                         //
        array[i] = nums.Next(1, 100);         //    Создание и наполнение массива
        Console.Write("| " + array[i] + " "); //
    }
    Console.WriteLine ("|");
    
    int counts = 0;

    for (int i = 0; i < array.Length; i++)    //  Поиск элементов в массиве на отрезке от 20 до 90
        
        if (array[i] % 2 == 0)   //
        {
            counts++;
            Console.Write("| " + array[i] + " ");

              }
    Console.WriteLine("|");
    Console.WriteLine(counts);
