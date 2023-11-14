// Caio Cesar 13/11/23
// BEE 1002

#include <stdio.h>
#include <stdlib.h>

int main() {

    double pi, raio, area;
    
    pi = 3.14159;

    scanf("%lf", &raio);

    area = pi * (raio*raio);

    printf("A=%.4lf\n", area);

    return 0;

}