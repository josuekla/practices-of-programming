#include <stdio.h>
#include <windows.h>
int main(void){
    int duracao;
    printf("Digite a duracao em segundos: ");
    scanf("%d", &duracao);
    while (duracao >= 0)
    {
        int hora = duracao / 3600;
        int resto = duracao % 3600;
        int minutos = resto / 60;
        int segundos = resto % 60;
        
        printf("%02d:%02d:%02d\n", hora, minutos, segundos);
        fflush(stdout);  
        duracao -= 1;
        Sleep(1000);
        system("cls");
    }
    
    
    printf("FIM");
    Sleep(3000);
    return 0;
}