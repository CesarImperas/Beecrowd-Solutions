// Caio Cesar 14/11/23
// BEE 1006

#include <iostream>

int main() {

    double notaA, notaB, notaC, media;
    scanf("%lf", &notaA);
    scanf("%lf", &notaB);
    scanf("%lf", &notaC);

    media = ((notaA * 2) + (notaB * 3) + (notaC * 5)) / 10;

    printf("MEDIA = %.1lf\n", media);

    return 0;
}