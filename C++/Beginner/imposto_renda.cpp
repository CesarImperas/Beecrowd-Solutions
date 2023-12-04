// Caio Cesar 01/12/23
// BEE 1051

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float salario, imposto;

    cin >> salario;
    cout << setprecision(2) << fixed;

    if(salario <= 2000.0){
        cout << "Isento" << endl;
    }else if(salario > 2000.0 && salario <= 3000.0){
        imposto = (salario - 2000) * 0.08;
        cout << "R$ " << imposto << endl;
    }else if(salario > 3000.0 && salario <= 4500.0){
        imposto = ((salario - 3000) * 0.18) + (1000 * 0.08);
        cout << "R$ " << imposto << endl;
    }else{
        imposto = ((salario - 4500) * 0.28) + (1500 * 0.18) + (1000 * 0.08);
        cout << "R$ " << imposto << endl;
    }
    
    return 0;
}