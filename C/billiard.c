#include <stdio.h>
#include <math.h>

int main(){

   int size = 5;
   int array[size], i;
   while(1){
   
      for(i = 0; i < size; i++ ){
         scanf("%d", &array[i]);
      }
      
      if(array[0] == 0 && array[1] == 0 && array[2] == 0 &&  array[3] == 0 &&  array[4] == 0){
         break;
      }

      double a = array[0] * array[3];
      double b = array[1] * array[4];
      double c = sqrt(a * a + b * b);

      double angle = acos(a / c) * (180.0 / M_PI);
      printf("%.2f ", angle);
      printf("%.2f\n", c / array[2]);
      
   }
}
