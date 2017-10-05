#include <stdio.h>

int main(){
    int tests,noAds,ads,cost,net;
    scanf("%d", &tests);
    for(int i = 0; i < tests; i++){
        scanf("%d", &noAds);
        scanf("%d", &ads);
        scanf("%d", &cost);
        net = ads - cost;

        if(noAds > net){
                printf("%s\n", "do not advertise");
        }
        else if(noAds < net){
                printf("%s\n", "advertise");
        }
        else{
                printf("%s\n", "does not matter");
        }
    }
}

