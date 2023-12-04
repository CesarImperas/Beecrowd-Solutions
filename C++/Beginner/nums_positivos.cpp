// Caio Cesar 30/11/23
// BEE 1060

#include <iostream>
using namespace std;

int main(){
    int positivos = 0;
    float numeros;

    for(int cont = 0; cont < 6; cont++){
        cin >> numeros;
        if(numeros > 0){
            positivos++;
        }
    }

    cout << positivos << " valores positivos" << endl;

    return 0;
}