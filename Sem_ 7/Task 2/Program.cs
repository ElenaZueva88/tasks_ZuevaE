// Задача 2: Напишите программу вычисления функции Аккермана
// с помощью рекурсии. Даны два неотрицательных числа m и n.

static int  Ackermann(int m, int n){
    if (m == 0) return n+1;
    if (m > 0 && n == 0) return Ackermann(m-1, 1);
    if (m > 0 && n > 0) return Ackermann(m-1, Ackermann(m,n-1));
    return Ackermann(m,n);
}

int result = Ackermann(2,3);
Console.WriteLine(result);



