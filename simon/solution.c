#include <stdio.h>
#include <string.h>

int main() {
    char* simonSays = "simon says";
    int number;
    scanf("%d\n", &number);

    for(int i = 0; i < number; ++i) {
        char inputs[1001];
        fgets(inputs, 1001, stdin);
        if (strstr(inputs, simonSays) == inputs) {
            printf("%s\n", &inputs[11]);
        } 
        else {
            printf("\n");
        }
    }
}


