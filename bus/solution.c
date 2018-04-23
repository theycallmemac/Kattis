

#include <stdio.h>

int getInitialNum(int n, double n1, double n2, int counter){

   if(counter == n){
      return n2;
   }
   else{
       double n3 = (n2 * 2) + 0.5;
      return getInitialNum(n, n2, n3, counter+1);
   }

}

int main(){

   int n,i,num;
   scanf("%d", &n);

   for(i = 0; i < n; i++){
      scanf("%d", &num);
      int output = getInitialNum(num, 0.5, 0.5, 0);
      printf("%d\n", output);
   }

}
