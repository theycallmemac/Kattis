#include <stdio.h>
#include <math.h>

int main() {

    while (1) {

        int D;
        long long int V;

        scanf("%d %lld", &D, &V);

        if (D == 0){ 
        	break;
        }

        double d = D * D * D - (6 * (V / M_PI));
        double answer = pow(d, 1 / 3.0);

        printf("%.7lf\n", answer);
    }
}
