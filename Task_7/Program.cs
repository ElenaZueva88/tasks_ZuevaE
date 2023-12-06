// Задайте двумерный массив из целых чисел.
// Сформируйте новый одномерный массив, состоящий из 
// средних арифметических значений по строкам двумерного массива. 

double [] Average2dArray(int [,] array){ 
    double [] createdArray = new double [array.GetLength(0)]; 
    for(int i = 0; i<array.GetLength(0); i++){ 
        double count = 0; 
        for(int j = 0; j<array.GetLength(1); j++){ 
            count+=array[i,j]; 
            } 
            createdArray[i] = count/array.GetLength(0); 
            } 
            return createdArray; 
            }
