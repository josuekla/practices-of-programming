#include <stdio.h>
int main(void){
    float a, b, c;
    printf("Digite a medida A: ");
    scanf("%f", &a);

    printf("Digite a medida B: ");
    scanf("%f", &b);

    printf("Digite a medida C: ");
    scanf("%f", &c);

    float quadrado = a * a;
    float triangulo = (a * b) / 2;
    float trapezio = (a + b) * c / 2 ;

    printf("Area do QUADRADO = %.4f\n", quadrado);
    printf("Area do TRIANGULO = %.4f\n", triangulo);
    printf("Area do TRAPEZIO = %.4f", trapezio);
    return 0;
}