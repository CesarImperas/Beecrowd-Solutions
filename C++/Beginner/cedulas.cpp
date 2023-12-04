// Caio Cesar 18/11/23
// BEE 1018

#include <cstdio>

int main(){
    int dinheiro, nota100, nota50, nota20, nota10, nota5, nota2, nota1;
    scanf("%d", &dinheiro);
    printf("%d\n", dinheiro);

    nota100 = dinheiro / 100;
    dinheiro = dinheiro % 100;

    nota50 = dinheiro / 50;
    dinheiro = dinheiro % 50;

    nota20 = dinheiro / 20;
    dinheiro = dinheiro % 20;

    nota10 = dinheiro / 10;
    dinheiro = dinheiro % 10;

    nota5 = dinheiro / 5;
    dinheiro = dinheiro % 5;

    nota2 = dinheiro / 2;
    dinheiro = dinheiro % 2;

    nota1 = dinheiro;

    printf("%d nota(s) de R$ 100,00\n", nota100);
    printf("%d nota(s) de R$ 50,00\n", nota50);
    printf("%d nota(s) de R$ 20,00\n", nota20);
    printf("%d nota(s) de R$ 10,00\n", nota10);
    printf("%d nota(s) de R$ 5,00\n", nota5);
    printf("%d nota(s) de R$ 2,00\n", nota2);
    printf("%d nota(s) de R$ 1,00\n", nota1);

    return 0;

}