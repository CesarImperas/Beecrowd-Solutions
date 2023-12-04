// Caio Cesar 30/11/23
// BEE 1070

#include <iostream>
using namespace std;

int main(){
    int numero, cont = 0;

    cin >> numero;

    while(cont < 6){
        if(numero % 2 != 0){
            cout << numero << endl;
            cont += 1;
        }
        numero += 1;
    }

    return 0;
}