#include <stdio.h>
#include <string.h>
int main(void){
    char nome[20];
    float valorHora;
    int horasTrabalhadas;

    printf("Nome: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0';
    printf("Valor por hora: ");
    scanf("%f", &valorHora);
    printf("horas trabalhadas: ");
    scanf("%d", &horasTrabalhadas);

    float pagamento = valorHora * horasTrabalhadas;

    printf("O pagamento para o %s deve ser de %.2f", nome, pagamento);
    return 0;
}