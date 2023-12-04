// Caio Cesar 30/11/23
// BEE 1065

#include <iostream>
using namespace std;

int main(){
    int cont = 0;
    int numero;

    for(int i = 0; i < 5; i++){
        cin >> numero;
        if(numero % 2 == 0){
            cont += 1;
        }
    }

    cout << cont << " valores pares" << endl;

    return 0;
}