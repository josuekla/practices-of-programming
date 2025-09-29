#include <stdio.h>
int main(){
    int minutos;
    int extra;
    double total = 50.00;

    printf("Digite a quantidade de minutos: ");
    scanf("%d", &minutos);
    if (minutos > 100){
        extra = (minutos - 100) * 2;
        total = total + extra;
    }
    printf("Valor a pagar: %.2lf\n", total);
    

    return 0;
}