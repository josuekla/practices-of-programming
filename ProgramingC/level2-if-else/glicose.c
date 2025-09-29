#include <stdio.h>
int main(){
    float glicose;
    printf("Digite a medida da glicose: ");
    if(scanf("%f", &glicose) != 1){
        printf("Entrada inválida. Por favor, digite um número.\n");
        return 1;
    }

    printf("Classificação: ");
    if(glicose <= 90){
        printf(" Normal\n");
    }
    else if(glicose <= 140){
        printf(" Elevado\n");
        
    }
    else{
        printf("Diabetes\n");

    }
}