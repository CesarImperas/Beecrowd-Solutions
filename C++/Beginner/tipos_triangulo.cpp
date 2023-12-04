// Caio Cesar 30/11/23
// BEE 1045

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    float A, B, C;

    cin >> A >> B >> C;

    vector<float> triangulos = {A, B, C};

    sort(triangulos.begin(), triangulos.end());
    reverse(triangulos.begin(), triangulos.end());

    // Atribuindo os valores do maior para o menor
    A = triangulos[0];
    B = triangulos[1];
    C = triangulos[2];

    if(A >= B + C){
        cout << "NAO FORMA TRIANGULO" << endl;
    }else if((A*A) == (B*B) + (C*C)){
        cout << "TRIANGULO RETANGULO" << endl;
    }else if((A*A) > (B*B) + (C*C)){
        cout << "TRIANGULO OBTUSANGULO" << endl;
    }else if((A*A) < (B*B) + (C*C)){
        cout << "TRIANGULO ACUTANGULO" << endl;
    }

    if((A == B) && (B == C) && (A == C)){
        cout << "TRIANGULO EQUILATERO" << endl;
    }else if((A == B) || (B == C)){
        cout << "TRIANGULO ISOSCELES" << endl;
    }

    return 0;
}