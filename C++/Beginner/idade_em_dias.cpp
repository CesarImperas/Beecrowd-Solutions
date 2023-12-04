// Caio Cesar 18/11/23
// BEE 1020

#include <cstdio>

int main() {
    int dias, aux, meses, anos;
    scanf("%d", &dias);

    aux = dias % 365;
    anos = dias / 365;
    meses = aux / 30;
    dias = aux % 30;

    printf("%d ano(s)\n", anos);
    printf("%d mes(es)\n", meses);
    printf("%d dia(s)\n", dias);

    return 0;

}