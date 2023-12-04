// Caio Cesar 02/12/23
// BEE 1151

#include <iostream>
#include <vector>
using namespace std;

int main(){
    unsigned int num_N, valor1, valor2;
    int indice1 = 0, indice2 = 1;
    vector<int> lista = {0, 1};

    cin >> num_N;

    while(lista.size() < num_N){
        valor1 = lista[indice1];
        valor2 = lista[indice2];
        lista.push_back(valor1 + valor2);
        indice1++;
        indice2++;
    }

    for(unsigned int i = 0; i < num_N; i++){
        if(i == num_N - 1){
            cout << lista[i] << endl;
        }else{
            cout << lista[i] << " ";
        }
    }

    return 0;
}