#include <stdio.h>

int main() {
    char month[3];
    int date;
    scanf("%s %d", month, &date);
    puts((month[0] == 'O' && date == 31)|| (month[0] == 'D' && date == 25) ? "yup" : "nope");
}
