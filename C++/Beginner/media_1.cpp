// Caio Cesar 14/11/23
// BEE 1005

#include <iostream>

int main() {

    double notaA, notaB, media;
    scanf("%lf", &notaA);
    scanf("%lf", &notaB);

    media = ((notaA * 3.5) + (notaB * 7.5)) / 11;

    printf("MEDIA = %.5lf\n", media);

    return 0;
}