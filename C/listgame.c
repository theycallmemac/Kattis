#include <stdio.h>

int x,i,k,y = 0;
int main(void){

	scanf("%d", &x);
  
	for (i = 1; i * i <= x; i++){
  
		if (x % i == 0){
			x = x / i;
			y++;
			i = 1;
		}
    
		if (x == 1){
			y++;
		}
	}
  
	k = y;
	printf("%d", k);
}
