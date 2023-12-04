// Caio Cesar 29/11/23
// BEE 1048

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float salario, porcentagem, reajuste, novo_salario;

    cin >> salario;

    if(salario >= 0 && salario <= 400){
        porcentagem = 0.15;
    }else if(salario >= 400.01 && salario <= 800){
        porcentagem = 0.12;
    }else if(salario >= 800.01 && salario <= 1200){
        porcentagem = 0.10;
    }else if(salario >= 1200.01 && salario <= 2000){
        porcentagem = 0.07;
    }else{
        porcentagem = 0.04;
    }

    reajuste = porcentagem * salario;
    novo_salario = reajuste + salario;

    cout << fixed << setprecision(2);
    cout << "Novo salario: " << novo_salario << endl;
    cout << "Reajuste ganho: " << reajuste << endl;
    cout << fixed << setprecision(0);
    cout << "Em percentual: " << porcentagem*100 << " %" << endl;

    return 0;
}