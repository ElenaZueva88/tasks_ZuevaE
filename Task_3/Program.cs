// Задача 3: Задайте массив из вещественных чисел с ненулевой дробной частью.
// Найдите разницу между максимальным и минимальным элементов массива.

static double[] CreateRandomArray(int min, int max, int size)
{
    double[] array = new double[size]; 
        Random ran = new Random();
        for (int i = 0; i < size; i++)
        {
                array[i] = Math.Round(ran.NextDouble() * (max - min) + min, 2);
        }
    return array;
}
static double DifferenceArrayElements(double[] array)
{
    double maxOf = array.Max();
    double minOf = array.Min();
    double result = maxOf - minOf;

    return Math.Round(result, 2);

}        
static void ShowArray(double[] array)
{
    
        for (int i = 0; i < array.Length; i++)
        {
            Console.Write(array[i] + "|");
        }

}
    double[] myArray = CreateRandomArray(0, 99, 15);
        double counts = DifferenceArrayElements(myArray);
            ShowArray(myArray);
                Console.WriteLine($"\nРазница между максимальным и минимальным элементом массива '{counts}'.");   
    


