#include <stdio.h>
#include <string.h>
int main(void){
    float distancia, combustivel;

    printf("Distância percorrida: ");
    scanf("%f", &distancia);

    printf("Combustível Gasto: ");
    scanf("%f", &combustivel);

    float Consumo = distancia / combustivel;
    printf("Consumo medio: %.3f", Consumo);
    return 0;
}