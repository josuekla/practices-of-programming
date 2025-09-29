#include <stdio.h>

int main(){
    double nota1, nota2, soma;

    printf("Digit the First Grade: ");
    scanf("%lf", &nota1); 
    printf("Digit the Second Grade: ");
    scanf("%lf", &nota2); 
    soma = nota1 + nota2;
    printf("NOTA FINAL = %.2lf\n", soma);
    if(soma < 60.00){
        printf("REPROVADO!\n");
    };


    return 0;
}