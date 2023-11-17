// Caio Cesar 16/11/23
// BEE 1010

#include <cstdio>

int main() {

    int codigo, quantidade;
    float valor_unitario, valor_total = 0;

    scanf("%d %d %f", &codigo, &quantidade, &valor_unitario);
    valor_total += (quantidade * valor_unitario);

    codigo = 0, quantidade = 0, valor_unitario = 0;

    scanf("%d %d %f", &codigo, &quantidade, &valor_unitario);

    valor_total += (quantidade * valor_unitario);

    printf("VALOR A PAGAR: R$ %.2f\n", valor_total);

    return 0;
}