// Задача 1: Напишите программу, которая бесконечно запрашивает целые числа с консоли.
// Программа завершается при вводе символа ‘q’ или при вводе числа, сумма цифр которого чётная.
while (true){
 Console.Write("Enter a number or 'q' to exit: ");
string input = Console.ReadLine(); 
  if (input == "q") {
break;
  }
int number;
 if (int.TryParse(input, out number)) {
  int sum = 0;
while (number > 0) 
{
sum += number % 10; 
number /= 10;
}
if (sum % 2 == 0) 
 {
Console.WriteLine("[EXIT]");
break;
 }
}
else {
Console.WriteLine("Incorrect input. Please enter an integer or 'q'.");
}
}


// while (true) // Бесконечный цикл
// {
// Console.Write("Введите число или 'q' для выхода: ");
// string input = Console.ReadLine(); // Чтение строки ввода пользователя
// if (input == "q") // Проверка на ввод 'q' для выхода
// {
// break;
// }
// int number;
// if (int.TryParse(input, out number)) // Проверка, является ли ввод числом
// {
// int sum = 0;
// while (number > 0) // Вычисление суммы цифр числа
// {
// sum += number % 10; // Добавление последней цифры к сумме
// number /= 10; // Удаление последней цифры из числа
// }
// if (sum % 2 == 0) // Проверка, является ли сумма цифр четной
// {
// Console.WriteLine("[STOP]");
// break;
// }
// }
// else // Если ввод не является числом и не 'q', повторить запрос
// {
// Console.WriteLine("Некорректный ввод. Пожалуйста, введите целое число
// или 'q'.");
// }
// }





