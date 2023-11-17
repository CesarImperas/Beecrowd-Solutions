// Caio Cesar 16/11/23
// BEE 1009

#include <cstdio>

int main() {

    char nome[20];
    double salario_fixo, vendas, salario_bonus;

    scanf("%[^\n]", nome);
    scanf("%lf", &salario_fixo);
    scanf("%lf", &vendas);

    salario_bonus = (vendas * 0.15) + salario_fixo;

    printf("TOTAL = R$ %.2lf\n", salario_bonus);

    return 0;
}