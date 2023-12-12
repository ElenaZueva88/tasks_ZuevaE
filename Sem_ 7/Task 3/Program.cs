// Задача 3: Задайте произвольный массив. Выведете его элементы, начиная с конца.
// Использовать рекурсию, не использовать циклы.
Console.Clear();

int [] arrayelem = new int [] {1, 2, 3};

static void  ShowArray(int [] array, int i = 0){ 
    if (i < array.Length){
        ShowArray(array, i + 1);
        Console.Write(array [i] + " ");
    }
}

ShowArray(arrayelem);



