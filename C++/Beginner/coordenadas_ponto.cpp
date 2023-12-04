// Caio Cesar 29/11/23
// BEE 1041

#include <iostream>
#include <string>
using namespace std;

int main(){
    float x, y;
    string resposta;

    scanf("%f %f", &x, &y);

    if(x == 0 && y == 0){
        resposta = "Origem";
    }else if((x == 0 && y > 0) || (x == 0 && y < 0)){
        resposta = "Eixo Y";
    }else if((x > 0 && y == 0) || (x < 0 && y == 0)){
        resposta = "Eixo X";
    }else if(x > 0 && y > 0){
        resposta = "Q1";
    }else if(x < 0 && y > 0){
        resposta = "Q2";
    }else if(x < 0 && y < 0){
        resposta = "Q3";
    }else if(x > 0 && y < 0){
        resposta = "Q4";
    }

    cout << resposta << endl;

    return 0;
}