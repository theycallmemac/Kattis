#include <stdio.h>
#include <string.h>

int main() {

    char in[305];
    scanf("%s", in);

    int i;
    int answer = 0;
    int len = strlen(in);
    
    for (i = 0; i < len; ++i) {
        if (i % 3 == 0 && in[i] != 'P') answer++;
        if (i % 3 == 1 && in[i] != 'E') answer++;
        if (i % 3 == 2 && in[i] != 'R') answer++;
    }

    printf("%d\n", answer);
    return 0;
}
