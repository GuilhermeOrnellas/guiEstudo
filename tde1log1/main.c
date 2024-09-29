#include<stdio.h>
int main(void) {
// 1
    // int v1, v2;

    // printf("digite um numero");
    // scanf("%d",&v1);
    // printf("digite outro numero");
    // scanf("%d",&v2);

    // v1+=v2;
    // v2=v1-v2;
    // v1-=v2;

    // printf("v1 = %d, v2 = %d\n", v1, v2);

// 2
    int numero, ant, suc;

    printf("digite um numero");
    scanf("%d",&numero);
    suc = numero++;
    ant = numero--;
    


    return 0;
}