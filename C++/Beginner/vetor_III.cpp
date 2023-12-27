// Caio Cesar 24/12/23
// BEE 1178

#include <iostream>
using namespace std;

int main(){
    double numero;

    int vect[1000];

    cin >> numero;

    for(int i=0; i<100; i++){
        printf("N[%d] = %.4lf\n", i, numero);

        numero /= 2.0;
    }

    return 0;
}