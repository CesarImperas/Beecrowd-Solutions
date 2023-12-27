// Caio Cesar 24/12/23
// BEE 1156

#include <cstdio>
using namespace std;

int main(){
    double soma = 0, denominador = 1;

    for(int numerador = 1;numerador <= 39; numerador += 2){
        soma += ((double) numerador / denominador);
        denominador *= 2;

    }

    printf("%.2lf\n", soma);

    return 0;
}