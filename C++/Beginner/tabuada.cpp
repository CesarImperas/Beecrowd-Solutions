// Caio Cesar 01/12/23
// BEE 1078

#include <iostream>
using namespace std;

int main(){
    int numero;

    cin >> numero;

    for(int tabuada = 1; tabuada < 11; tabuada++){
        cout << tabuada << " x " << numero << " = " << numero*tabuada << endl;
    }

    return 0;
}