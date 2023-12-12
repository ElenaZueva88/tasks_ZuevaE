// Задача 1: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа
//  в промежутке от M до N. Использовать рекурсию, не использовать циклы.
                                 //5   //15
static void FuncNaturNums(int m, int n) {
    if (m <= n){
       FuncNaturNums(m, n - 1);
        Console.Write(n + " ");
    }
   }

FuncNaturNums(10,80);

