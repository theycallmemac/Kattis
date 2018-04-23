#include <stdio.h>
#include <string.h>

int main() {

	int n;
	scanf("%d\n", &n);

	for(int i = 0; i < n; i++){

		char space = ' ';
		long int length = 0;

		while(1) {
			scanf("%c", &space);
			if(space == '\n') {
				break;
			}
			length++;
		}
		printf("%ld\n", length);
	}
    
}


