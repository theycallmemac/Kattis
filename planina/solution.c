#include <stdio.h>

int main() {

	int num = 0;
  scanf("%d", &num);
  double p = 2;
  
  for (int i = 0; i < num; i++)
      p = p + p - 1;

  printf("%.0lf\n", p * p);
  return 0;
    
}

