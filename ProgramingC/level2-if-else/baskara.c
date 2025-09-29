#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main(){
    double a, b, c, delta, xmais, xmenos;
    printf("Coeficiente a: \n");
    scanf("%lf", &a);
    printf("Coeficiente b: \n");
    scanf("%lf", &b);
    printf("Coeficiente c: \n");
    scanf("%lf", &c);

    delta = pow(b, 2) - (4 * a * c);
    if (delta < 0){
        printf("Esta equacao nao possui raizes reais \n");
        exit(0);
    }
    xmais = (-b + sqrt(delta)) / (2 * a);
    xmenos = (-b - sqrt(delta)) / (2 * a);
    
    printf("X1 = %.4lf\n", xmais);
    printf("X2 = %.4lf\n", xmenos);

    printf("\n\n");
    printf("Finish program with Success!\n\n");
    return 0;
}