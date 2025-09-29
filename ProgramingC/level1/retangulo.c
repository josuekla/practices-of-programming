#include <stdio.h>
#include <math.h>

int main(void){
    float BaseRentangulo, AlturaRentangulo;

    printf("Base do retangulo: \n");
    scanf("%f", &BaseRentangulo);

    printf("Altura do retangulo: \n");
    scanf("%f", &AlturaRentangulo);

    float area = BaseRentangulo * AlturaRentangulo;
    float perimetro = 2*(BaseRentangulo + AlturaRentangulo);
    float diagonal = sqrt(BaseRentangulo * BaseRentangulo + AlturaRentangulo * AlturaRentangulo);

    printf("AREA: %.4f\n", area);
    printf("PERIMETRO: %.4f\n", perimetro);
    printf("DIAGONAL: %.4f\n", diagonal);

    return 0;
}