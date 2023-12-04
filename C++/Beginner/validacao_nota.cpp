// Caio Cesar 29/11/23
// BEE 1048

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int contador = 0;
    float soma, nota, media;

    while(contador < 2){
        cin >> nota;
        if(nota >= 0 && nota <= 10){
            soma += nota;
            contador++;
        }else{
            cout << "nota invalida" << endl;
        }
    }

    media = soma / 2.0;

    cout << "media = " << media << setprecision(2) << fixed << endl;

    return 0;
}