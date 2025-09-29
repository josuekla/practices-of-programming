#include<stdio.h>

int main()
{
    int a,b;
    printf("Digite dois numeros inteiros: \n");
    scanf("%d", &a);
    scanf("%d", &b);
    if (a == 0 || b == 0) {
        printf("Não é possível verificar múltiplos com zero.\n");
    } else if (a % b == 0 || b % a == 0) {
        printf("São múltiplos\n");
    } else {
        printf("Não são múltiplos\n");
    }
    
    return 0;
}