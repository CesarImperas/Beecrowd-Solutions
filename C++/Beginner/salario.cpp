// Caio Cesar 16/11/23
// BEE 1008

#include <cstdio>

int main() {
    
    int funcionarios, horas;
    float recebe_horas, salario;

    scanf("%d", &funcionarios);
    scanf("%d", &horas);
    scanf("%f", &recebe_horas);

    salario = recebe_horas * horas;

    printf("NUMBER = %d\n", funcionarios);
    printf("SALARY = U$ %.2f\n", salario);

    return 0;
}