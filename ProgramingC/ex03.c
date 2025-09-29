#include <stdio.h>

int main (void){
    char produto1[] = "Computador";
    char produto2 = "TV";
    float preco1 = 3200.5; 
    float preco2 = 1200.0; 
    int idade = 30;
    int codigo = 5291;
    char genero = 'F';

    printf("Produtos: \n");
    printf("O produto %s custa R$ %f \nO produto %s custa R$ %f", produto1, preco1, produto2, preco2);
    printf("Código:  %cd \n", codigo);
    printf("Dados da pessoa: Genero %c e idade %d", genero, idade );
}