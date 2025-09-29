#include <stdio.h>

int main(void){
    #define PI 3.14159265358979323846 
    float raioCirculo;
    
    printf("Digite o valor do raio do circulo: ");
    scanf("%f", &raioCirculo);

    float area = PI * (raioCirculo * raioCirculo);
    
    printf("AREA: %.3f", area);
    return 0;
}