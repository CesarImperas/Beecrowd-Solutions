// Caio Cesar 25/12/23
// BEE 3346

#include <cstdio>

int main(){
    double f1, f2, flutuacao;

    scanf("%lf", &f1);
    scanf("%lf", &f2);

    flutuacao = (((1 + (f1/100.0)) * (1 + (f2/100.0))) - 1) * 100.0;

    printf("%.6f\n", flutuacao);

    return 0;
}