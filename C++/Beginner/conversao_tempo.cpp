// Caio Cesar 18/11/23
// BEE 1019

#include <cstdio>

int main(){
    int tempo, horas, minutos, segundos;
    scanf("%d", &tempo);

    horas = tempo / 3600;
    tempo %= 3600;
    minutos = tempo / 60;
    segundos = tempo % 60;

    printf("%d:%d:%d\n", horas, minutos, segundos);

    return 0;

}