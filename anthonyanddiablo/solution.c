#include <stdio.h>
#define M_PI 3.14159265358979323846
int main() {
    double a;
    double n;
    scanf("%lf %lf", &a, &n);
    double radius = n / (2 * M_PI);
    double area = M_PI * (radius * radius);
    if (area > a) {
        printf("%s\n", "Diablo is happy!");
    } else {
        printf("%s\n", "Need more materials!");
    }
}
