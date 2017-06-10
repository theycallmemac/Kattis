#include <stdio.h>

int main() {

    int k;
    scanf("%d", &k);
    long long int a = 1, b = 0;

    while (0 < k) {
    
        long long int numA = b;
        long long int numB = a + b;
        a = numA;
        b = numB;
        k = k - 1;
        
    }
    
    printf("%lld %lld\n", a, b);
    
}
