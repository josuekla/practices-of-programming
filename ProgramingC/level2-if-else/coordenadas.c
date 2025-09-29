#include <stdio.h>
int main(){
    float x, y;
    char *destino;
    printf("Valor de X: " );
    scanf("%f", &x);
    printf("Valor de y: " );
    scanf("%f", &y);
    if(x == 0 || y == 0){
        if(y !=  0){
            destino = "Eixo Y";
        } else if(x != 0 ){
            destino = "Eixo X";
        } else{
            destino = "Origem";
        }
    } else if( x > 0){
        if (y > 0){
            destino = "Q1";
        } else{
            destino = "Q4";
        }
    } else{ 
        if ( y > 0){
            destino = "Q2";
        } else{
            destino = "Q3";
        }
    } 
        
    printf("%s\n", destino);
    return 0;
}