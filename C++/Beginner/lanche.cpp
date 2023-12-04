// Caio Cesar 28/11/23
// BEE 1038

#include <cstdio>

int main(){
    int codigo, quantidade;
    float valor;

    scanf("%d %d", &codigo, &quantidade);

    if(codigo == 1){
        valor = quantidade * 4.0;
    }else if(codigo == 2){
        valor = quantidade * 4.5;
    }else if(codigo == 3){
        valor = quantidade * 5.0;
    }else if(codigo == 4){
        valor = quantidade * 2.0;
    }else{
        valor = quantidade * 1.5;
    }

    printf("Total: R$ %.2f\n", valor);

    return 0;    
}