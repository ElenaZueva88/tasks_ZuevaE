//Задайте двумерный массив размера i на j, каждый элемент в 
//массиве находится по формуле: Aₘₙ = i+j. 
//Выведите полученный массив на экран. 

int [,] SumArray(int row, int col){ 
    int [,] array = new int [row,col];
     for(int i=0;i<row;i++){ 
        for(int j=0;j<col;j++){ 
            array[i,j] = i+j; 
        } 
    } 
            return array; 
            }
