#include <stdio.h>

int main(){
    int hrInicial, hrFinal, duracao;
    printf("Hora inicial: ");
    scanf("%d", &hrInicial);
    printf("Hora final: ");
    scanf("%d", &hrFinal);

    if(hrInicial > hrFinal){
        duracao = 24 - (hrInicial - hrFinal);
    } else if(hrInicial < hrFinal){
        duracao = hrFinal - hrInicial;
    } else{
        duracao = 24;
    }

    printf("O JOGO DUROU %d HORA(S)\n", duracao);
    printf("Pressione qualquer tecla para sair...\n");

    // Consome a tecla pressionada
    getchar();
    getchar();

    return 0;
}