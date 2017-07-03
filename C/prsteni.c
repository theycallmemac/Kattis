#include <stdio.h>

int main() {

    int rings,a,b,gcd,array[105];
    scanf("%d", &rings);
    for (int i = 0; i < rings; i++) {
        scanf("%d", &array[i]);
    }

    for (int j = 1; j < rings; j++) {
        a = array[0];
        b = array[j];

        for(int k = 1; k <= a && k <= b; k++)
        {
            if(a % k == 0 && b % k == 0)
            gcd = k;
        }

        a /= gcd;
        b /= gcd;

        printf("%d/%d\n", a, b);
    }
}
