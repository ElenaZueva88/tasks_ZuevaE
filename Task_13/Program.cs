// Задача 3: Напишите программу, которая перевернёт одномерный массив
// (первый элемент станет последним, второй – предпоследним и т.д.)
int[] array = new int[10]; 
    Random nums = new Random();
    for (int i = 0; i < array.Length; i++)    
    {                                         
        array[i] = nums.Next(1, 10);          //    Создание и наполнение массива
        Console.Write("| " + array[i] + " "); 
    }
    Console.WriteLine ("|");

Array.Reverse(array);                       //    Метод разворота массива
for (int i = 0; i < array.Length; i++)
{
    Console.Write("| " + array[i] + " ");
}
Console.WriteLine ("|");


// int[] numbers = {1, 3, 5, 6, 7, 8}; // Исходный массив
// int temp;
// // Вывод исходного массива
// Console.Write("Исходный массив: ");
// foreach (int number in numbers)
// {
// Console.Write(number + " ");
// }
// // Реверсирование массива
// for (int i = 0; i < numbers.Length / 2; i++)
// {
// // Меняем местами элементы
// temp = numbers[i];
// numbers[i] = numbers[numbers.Length - 1 - i];
// numbers[numbers.Length - 1 - i] = temp;
// }
// // Вывод измененного массива
// Console.Write("\nПеревернутый массив: ");
// foreach (int number in numbers)
// {
// Console.Write(number + " ");
// }





