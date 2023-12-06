// Задайте массив из 10 элементов, заполненный числами из промежутка [-10, 10]. 






// Замените отрицательные элементы на положительные, а положительные на отрицательные. 
int [] CreateArray(int max, int min, int size) {
     int [] array = new int [size]; for(int i = 0; i<size; i++){
         array[i] = new Random().Next(min, max+1); 
    } 
    return array; 
} 
    void ShowArray(int [] array){
         for(int i = 0; i<array.Length;i++){
 Console.Write(array[i] +" "); 
} 
 Console.WriteLine(); 
} 
void ShowReverseArray(int [] array){ 
    for(int i = 0; i < array.Length; i++) { 
        array[i] = -array[i]; Console.Write(array[i] + " "); 
 } 
 } 
 Console.WriteLine("Enter array size"); 
 int size = Convert.ToInt32(Console.ReadLine()); 
 Console.WriteLine("Enter array min"); 
 int min = Convert.ToInt32(Console.ReadLine()); 
 Console.WriteLine("Enter array max"); 
 int max = Convert.ToInt32(Console.ReadLine()); 
 int [] array = CreateArray(max, min, size); 
 ShowArray(array); ShowReverseArray(array);
