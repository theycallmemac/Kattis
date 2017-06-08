#include <stdio.h>
int main( ) {

   int i;
   int j;
   int k;

   scanf("%d %d", &i, &j);

   k = i * (j-1) + 1;
   printf("%d", k);

   return 0;
}
