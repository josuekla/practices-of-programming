#include <stdio.h>

int main(){
    int n;
    int values[7] = {0};

    scanf("%d", &n);
    while (n != 0){
        if (n >= 100){
            values[0] += 1;
            n -= 100;
        }
        else if(n >= 50){ 
            values[1] += 1;
            n -= 50;
        }
        else{
            if (n >= 20){
                values[2] += 1;
                n -= 20;
            }
            else if(n >= 10){
                values[3] += 1;
                n -= 10;
            }
            else if(n >= 5){
                values[4] += 1;
                n -= 5;
            }
            else if(n >= 2){
                values[5] += 1;
                n -= 2;
            }
            else{
                values[6] += 1;
                n -= 1;
            }
        }
        
        
    }


    	
    printf("%d nota(s) de R$ de 100,00\n", values[0]);
    printf("%d nota(s) de R$ de 50,00\n", values[1]);
    printf("%d nota(s) de R$ de 20,00\n", values[2]);
    printf("%d nota(s) de R$ de 10,00\n", values[3]);
    printf("%d nota(s) de R$ de 5,00\n", values[4]);
    printf("%d nota(s) de R$ de 2,00\n", values[5]);
    printf("%d nota(s) de R$ de 1,00\n", values[6]);

    return 0;
}