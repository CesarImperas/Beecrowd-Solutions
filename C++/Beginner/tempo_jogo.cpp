// Caio Cesar 29/11/23
// BEE 1047

#include <iostream>
using namespace std;

int main(){
    int hora_ini, hora_fim, tempo;

    cin >> hora_ini >> hora_fim;

    if(hora_ini >= hora_fim){
        tempo = 24 - hora_ini + hora_fim;
        cout << "O JOGO DUROU " << tempo << " HORA(S)" << endl;
    }else{
        tempo = hora_fim - hora_ini;
        cout << "O JOGO DUROU " << tempo << " HORA(S)" << endl;
    }

    return 0;
}