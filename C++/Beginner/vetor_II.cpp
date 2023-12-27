// Caio Cesar 24/12/23
// BEE 1177

#include <iostream>
using namespace std;

int main(){
    int n, contador = 0;

    int vect[1000];

    cin >> n;

    for(int i=0; i<1000; i++){
        printf("N[%d] = %d\n", i, contador);

        contador++;

        if(contador == n){
            contador = 0;
        }
    }

    return 0;
}