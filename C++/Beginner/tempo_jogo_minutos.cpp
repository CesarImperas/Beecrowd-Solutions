// Caio Cesar 29/11/23
// BEE 1047

#include <iostream>
using namespace std;

int main(){
    int h1, min1, h2, min2, tempo1, tempo2, tempo_total, htotal, mintotal;

    cin >> h1 >> min1 >> h2 >> min2;

    tempo1 = (h1*60) + min1;
    tempo2 = (h2*60) + min2;

    tempo_total = tempo2 - tempo1;

    if(tempo_total <= 0){
        tempo_total += (24*60);
    }

    htotal = tempo_total / 60;
    mintotal = tempo_total % 60;

    cout << "O JOGO DUROU " << htotal << " HORA(S) E " << mintotal << " MINUTO(S)" << endl;

    return 0;
}