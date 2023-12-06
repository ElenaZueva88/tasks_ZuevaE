int[] CreateNewArray(int[] array) {
     int[] result = new int[array.Length / 2 + array.Length % 2]; 
     int length = array.Length / 2; 
     for (int i = 0; i < length; i++) { 
      result[i] = array[i] * array[array.Length - i - 1];
} 
if (array.Length % 2 > 0) { 
    result[length] = array[length];
} return result; 
} 
Console.WriteLine("Enter array size"); 
int size = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine("Enter array min"); 
int min = Convert.ToInt32(Console.ReadLine()); 
Console.WriteLine("Enter array max"); 
int max = Convert.ToInt32(Console.ReadLine()); 
int[] arr = CreateArray(max, min, size); 
ShowArray(arr); int[] newArr = CreateNewArray(arr); 
ShowArray(newArr);

void Test(int num) {
    int count = 0; int num1 = num; 
    while (num1 != 0) { num1 = num1 / 10;
    count++; }
    int[] array = new int[count];
    for (int i = 0; i < count; i++)







