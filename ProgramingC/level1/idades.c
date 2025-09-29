#include <stdio.h>
#include <string.h>

int main(void){
    char nome1[50];
    float idade1;
    char nome2[50];
    float idade2;

    printf("Dados da primeira pessoa: \n");
    printf("Nome: \n");
    fgets(nome1, 50, stdin);
    nome1[strcspn(nome1, "\n")] = '\0';

    printf("Idade: \n");
    scanf("%f", &idade1);
    getchar();

    printf("Dados da segunda pessoa: \n");
    
    printf("Nome: \n");
    fgets(nome2, 50, stdin);
    nome2[strcspn(nome2, "\n")] = '\0';
    printf("Idade: \n");
    scanf("%f", &idade2);

    float media = (idade1 + idade2) / 2;
    printf("A idade média de %s e %s é de %.1f", nome1, nome2, media);

    return 0;
}