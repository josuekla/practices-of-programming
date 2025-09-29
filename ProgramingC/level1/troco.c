#include <stdio.h>

int main(void){
     int quantidadeComprada;
     float precoUnitario, DinheiroRecebido;

     printf("Preço unitario por produto: ");
     scanf("%f", &precoUnitario);

     printf("Quantidade comprada: ");
     scanf("%d", &quantidadeComprada);

     printf("Dinheiro recebido: ");
     scanf("%f", &DinheiroRecebido);

     float troco = DinheiroRecebido - (quantidadeComprada * precoUnitario);

     printf("TROCO: %.2f", troco);
}