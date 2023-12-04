// Caio Cesar 30/11/23
// BEE 1064

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int cont = 0, positivos = 0;
    float soma = 0, media, entrada;

    while(cont < 6){
        cont += 1;
        cin >> entrada;
        if(entrada > 0){
            soma += entrada;
            positivos += 1;
        }
    }

    media = soma / positivos;

    cout << positivos << " valores positivos" << endl;
    cout << fixed << setprecision(1) << media << endl;

    return 0;
}