#include <stdio.h>
#include <limits.h> // Função paara usar o maior número o possível

int main(){
    int a, b, c;
    int lista[3];
    int menor = INT_MAX;
    printf("Primeiro valor: ");
    scanf("%d", &lista[0]);
    printf("Segundo valor: ");
    scanf("%d", &lista[1]);
    printf("Terceiro valor: ");
    scanf("%d", &lista[2]);

    for (int i = 0; i < 3; i++){
        if(lista[i] < menor ){
            menor = lista[i];
        }

    }

    printf("MENOR = %d", menor);
    

    printf("\n\n");
    printf("Finish program with Success!\n\n");
    return 0;
}