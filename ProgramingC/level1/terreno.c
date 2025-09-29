#include <stdio.h>

int main (void) {
    float largura;
    float comprimento;
    float valorTerreno;
    


    printf("Digite a largura do terreno: \n");
    scanf("%f", &largura);
    printf("Digite o comprimento do terreno: \n");
    scanf("%f", &comprimento);
    printf("Digite o valor do metro quadrado: \n");
    scanf("%f", &valorTerreno);


    float areaTerreno = largura * comprimento;
    float valorTerrenoTotal = areaTerreno * valorTerreno;

    printf("Area do terreno = %.2f\n", areaTerreno);
    printf("Preço do terreno = %.2f", valorTerrenoTotal);

    return 0;

}