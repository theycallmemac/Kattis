#include <stdio.h>
int main () {
    int counts[5];
    char cards[14];
    scanf("%[^\n]s", &cards);
    for (int i = 0; i < sizeof(cards)/sizeof(cards[0]); i=i+3) {
        int count = 0;
        for (int j = 0; j < sizeof(cards)/sizeof(cards[0]); j=j+3) {
            if (cards[i] == cards[j]) {
                count++;
            }
        }
        if (i > 0) {
            counts[i/3] = count;
        } else {
            counts[i] = count;
        }
    }
    int max = counts[0];
    for (int k = 0; k < sizeof(counts)/sizeof(counts[0]); k++) {
        if (counts[k] > max) {
            max = counts[k];
        }
    }
    printf("%d\n", max);
}
