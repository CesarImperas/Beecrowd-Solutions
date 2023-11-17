// Caio Cesar 16/11/23
// BEE 1014

#include <cstdio>

int main() {

    int distancia;
    float combustivel, consumo;

    scanf("%d", &distancia);
    scanf("%f", &combustivel);

    consumo = distancia/combustivel;

    printf("%.3f km/l\n", consumo);

    return 0;
}