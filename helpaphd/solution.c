#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 0, i = 0;
    scanf("%d",&n);
    char eq[10];

    while(n--) {
        scanf("%s", eq);
        if (eq[0] == 'P') {
            printf("skipped\n");
            continue;
        }
        i = 0;
        while (*(eq + i) != '+') i++;
        eq[i] = '\0';
        printf("%d\n", atoi(eq) + atoi(eq + i + 1));
    }
    return 0;
}
