#include <stdio.h>

int shiftSuit(int* counts,  int num, char suit) {

    switch (suit) {
    case 'P':
        counts[0] -= 1;
        return num;
    case 'K':
        counts[1] -= 1;
        return num + 13;
    case 'H':
        counts[2] -= 1;
        return num + 26;
    case 'T':
        counts[3] -= 1;
        return num + 39;
    }
}

int main() {

    int cards[52] = {0};
    int counts[4] = {13, 13, 13, 13};
    int num;
    char suit;

    while (scanf("%c%d", &suit, &num) != EOF && suit != '\n') {
        num= shiftSuit(counts, num, suit);
        if (cards[num-1]) {
            printf("GRESKA\n");
            return 0;
        } else {
            cards[num-1] = 1;
        }
    }

    printf("%d %d %d %d\n", counts[0], counts[1], counts[2], counts[3]);

    return 0;
}
