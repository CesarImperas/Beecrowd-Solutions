// Caio Cesar 17/11/23
// BEE 1017

#include <cstdio>

int main() {
    int tempo, velocidaMedia;
    float litros;

    scanf("%d", &tempo);
    scanf("%d", &velocidaMedia);

    litros = (tempo * velocidaMedia)/12.0;

    printf("%.3f\n", litros);

    return 0;
}