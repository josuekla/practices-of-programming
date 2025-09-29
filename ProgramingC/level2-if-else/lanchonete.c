#include<stdio.h>

int main()
{
    int produto_escolhido;
    float quantidade, valor_total;
    printf("Codigo do produto comprado: ");
    scanf("%d", &produto_escolhido);
    printf("Quantidade comprada: ");
    scanf("%f", &quantidade);
    
    
    switch (produto_escolhido) {
        case 1:
            valor_total = quantidade * 5.0;
            break;
        case 2:
            valor_total = quantidade * 3.5;
            break;
        case 3:
            valor_total = quantidade * 4.8;
            break;
        case 4:
            valor_total = quantidade * 8.9;
            break;
        case 5:
            valor_total = quantidade * 7.32;
            break;
        default:
            printf("Código inválido. Digite um valor entre 1 e 5.\n");
            return 1;
    }
    
    printf("Valor a pagar: R$ %.2f\n", valor_total);
    return 0;
    
}