#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    float celsius, fahrenheit;
    char resposta;
    // celsius = (5/9) *
    printf("Voce vai digitar a temperatura em qual escala (C/F)?");
    scanf(" %c", &resposta);
    resposta = tolower(resposta);

    if(resposta == 'f'){

        printf("Digite a temperatura em Fahrenheit:");
        celsius = (5.0 / 9.0) * (fahrenheit - 32);
        printf("Temperatura equivalente em Celsius: %.2f", celsius);
    } else if (resposta == 'c'){
        printf("Digite a temperatura em Celsius:");
        scanf("%f", &celsius);
        fahrenheit = (celsius * 9/5) + 32;
        printf("Temperatura equivalente em Fahrenheit: %.2f", fahrenheit);
    }
    else{
        printf("Digite um valor válido");
    }
    

    printf("\n\n");
    return 0;
}