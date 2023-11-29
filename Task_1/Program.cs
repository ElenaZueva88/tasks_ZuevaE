/* Задача 1: Задайте одномерный массив из 10 целых чисел от 1 до 100. 
Найдите количество элементов массива, значения которых лежат в отрезке [20,90].
 */ 
int [] myArray = new int [] {10, 20, 30, 45, 14, 15, 16, 17, 18, 88};
int first = 0;
int second = 0; 

for (int i = 0; i < myArray.Length; i++) 
{
  if (myArray.Length [i] ) 

    int[] array = new int[10];
    Random nums = new Random();
}
    for (int i = 0; i < array.Length; i++)    //
    {                                         //
        array[i] = nums.Next(1, 100);         //    Создание и наполнение массива
        Console.Write("| " + array[i] + " "); //
    }
    Console.WriteLine ("|");
    
    int counts = 0;

    for (int i = 0; i < array.Length; i++)    //  Поиск элементов в массиве на отрезке от 20 до 90
        if (array[i] >=20 && array[i] <=90)   //
        {
            counts++;
            Console.Write("| " + array[i] + " ");
           
        }
    Console.WriteLine("|");
    Console.WriteLine(counts);




