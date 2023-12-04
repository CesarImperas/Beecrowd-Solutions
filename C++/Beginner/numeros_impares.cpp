// Caio Cesar 30/11/23
// BEE 1067

#include <iostream>
using namespace std;

int main(){
    int cont, numero;

    cin >> numero;

    if(numero >= 1 && numero <= 1000){
        for(cont = 1; cont < numero + 1; cont += 2){
            cout << cont << endl;
        }
    }

    return 0;
}