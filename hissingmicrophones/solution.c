#include <stdio.h>
int main(){
    char line[30];
    char hissy = 's';
    scanf("%s", line);
    int strLen = sizeof(line) / sizeof(line[0]);
    for(int i = 0; i < strLen; i++) {
        if (i + 1 == strLen) {
           printf("%s\n", "no hiss");
           break;
        }

        if (line[i] == hissy && line[i + 1] == hissy) {
            printf("%s\n", "hiss");
            break;
        }
    }
}
