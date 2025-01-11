#include <stdio.h>

int* maxfunc(int l, int r){
    int* abc[3];
    while (l < r){

    }
    return abc;
}

int main(){
    int t;
    scanf("%d", &t);

    for (int i = 0; i++; i<t){
        int l;
        int r;
        scanf("%d %d", &l, &r);
        int* abc = maxfunc(l, r);
        printf("%d %d %d", abc[0], abc[1], abc[2]);
    }

    return 0;
}