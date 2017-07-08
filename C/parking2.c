#include <stdio.h>

int main(){
	int tests, n, tmp, array[30];

	scanf("%d", &tests);

	for(int test = 0; test < tests; test++){
		scanf("%d", &n);
		for (int i = 0; i < n; ++i){
			scanf("%d", &array[i]);
			}

		for (int i = 0; i < n; ++i){
			for (int j = i + 1; j < n; ++j){
				if (array[i] > array[j]){
					tmp =  array[i];
					array[i] = array[j];
					array[j] = tmp;
					}
			}
		}
		printf("%d\n", (array[n - 1] - array[0]) * 2);
	}
}
