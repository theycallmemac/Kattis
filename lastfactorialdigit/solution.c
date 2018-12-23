#include <stdio.h>


int factorial(int n) {
    if (n == 1) {
        return n;
    } else {
        return n * factorial(n-1);
    }
}

int main() {
    int t, n;
    scanf("%d", &t);
    do {
        scanf("%d", &n);
        int x = factorial(n);
        t--;
        printf("%d\n", x % 10);
    } while (t > 0);
}
