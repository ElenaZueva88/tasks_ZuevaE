// Дано натуральное число в диапазоне от 1 до 100 000. Создайте массив, состоящий из цифр этого числа.
// Старший разряд числа должен располагаться на 0-м индексе массива, младший – на последнем. 
// Размер массива должен быть равен количеству цифр.

static int[] NumbersArray(int number)
{
    int count = 0;
    int first = number;

        while (first != 0) 
        {
                first = first / 10;
                count++;
        }

    int[] array = new int[count];

        for (int i = count - 1; i >= 0; i--)
        {
                array[i] = number % 10;
                number /= 10;
        }
    return array;
}
static void ShowArray(int[] array)
{
        for (int i = 0; i < array.Length; i++)
        {
            Console.Write(array[i] + "|");
        }
            Console.Write("\nВывод массива по указанному числу.");
}
    int[] myArray = NumbersArray(6789);
            ShowArray(myArray);
    







