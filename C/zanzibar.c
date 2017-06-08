#include <stdio.h>

int main() {

    int tests;
    scanf("%d", &tests);
    int test;

    for (test = 0; test < tests; test++) {

        long int i = 1;
        long long int notBorn = 0;

        while (0 < i) {
            long int j;
            scanf("%ld", &j);

            if (i*2 < j) {
                notBorn += j - i*2;
            }
            i = j;
        }
        printf("%lld\n", notBorn);
    }
    
}
