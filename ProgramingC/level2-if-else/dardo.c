// #include <stdio.h>

// int main(){
//     float d[3];
//     float maior = 0;
//     printf("Digite as três distãncia: \n");
//     for (int i = 0; i < 3 ; i++){
//         scanf("%f", &d[i]);
//         if(d[i] > maior){
//             maior = d[i];
//         }
//     }

//     printf("MAIOR DISTANCIA %.2fM\n", maior);

//     return 0;
// }


#include <stdio.h>

int main(){
    int m = 50;
    int *p = &m;

    printf("Conteudo da variavel: %p", &m);
    printf("endereço da variavel: %p", p);



    printf("\n\n");
}