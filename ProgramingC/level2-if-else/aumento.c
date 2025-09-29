#include <stdio.h>
int main(){
    float salario, novoSalario, porcentagem, aumento;
    printf("Digite o salario da pessoa: ");
    scanf("%f", &salario);
    if(salario <= 1000){
        porcentagem = 20;
    } else if (salario <= 3000){
        porcentagem = 15;
    } else if(salario <= 8000){
        porcentagem = 10;
    } else{
        porcentagem = 5;
    }

        aumento = salario * porcentagem / 100;
        novoSalario =  aumento + salario;

        printf("\n--- Reajuste Salarial ---\n");
        printf("Novo salario = R$ %.2f\n", novoSalario);
        printf("Aumento %.2f\n", aumento);
        printf("Porcentagem %.0f %%\n ", porcentagem);

    return 0;
}