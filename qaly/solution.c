#include <stdio.h>

int main() {
    float n, q, y, qaly, total = 0;
    scanf("%f", &n);
    do {
        scanf("%f %f", &q, &y);
        qaly = q * y;
        total += qaly;
        n--;
    } while(n > 0);
    printf("%.3f\n", total);
}
