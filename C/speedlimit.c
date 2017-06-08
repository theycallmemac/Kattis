#include <stdio.h>

int main() {

    while (1) {

        int num;
        scanf("%d", &num);

        if (num < 0) break;

        int i;
        long int answer = 0;
        int j = 0;

        for (i = 0; i < num; ++i) {
            int s, t;
            scanf("%d %d", &s, &t);
            answer += s*(t-j);
            j = t;
        }

        printf("%ld miles\n", answer);
    }
    return 0;
}
