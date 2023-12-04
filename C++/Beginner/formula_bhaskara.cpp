// Caio Cesar 28/11/23
// BEE 1036

#include <cstdio>
#include <cmath>

int main(){
    double numA, numB, numC, delta, x1, x2;

    scanf("%lf %lf %lf", &numA, &numB, &numC);

    delta = pow(numB, 2) - (4 * numA * numC);
    if(delta < 0 || numA == 0){
        printf("Impossivel calcular\n");
    }else{
        x1 = ((- numB) + sqrt(delta)) / (2.0 * numA);
        x2 = ((- numB) - sqrt(delta)) / (2.0 * numA);

        printf("R1 = %.5lf\n", x1);
        printf("R2 = %.5lf\n", x2);
    }

    return 0;
}