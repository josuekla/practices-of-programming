#include <stdio.h>

int main(){
    float precoUnitario, cashPay, change;
    int quantidadesUnidades;

    printf("Preço unitário do produto: ");
    scanf("%f", &precoUnitario);
    printf("Quantidade comprada: ");
    scanf("%d", &quantidadesUnidades);
    printf("Dinheiro recebido: ");
    scanf("%f", &cashPay);
    change = cashPay - (precoUnitario * quantidadesUnidades) ;
    
    if (change > 0){
        printf("TROCO = %.2f\n", change);
    } else{
        printf("DINHEIRO INSUFICIENTE. FALTAM %.2f REAIS \n", change * -1);

    }

    return 0;
}