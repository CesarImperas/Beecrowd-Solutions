// Caio Cesar 29/11/23
// BEE 1042

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int n1, n2, n3;
    scanf("%d %d %d", &n1, &n2, &n3);

    // Criação das duas listas
    int lista[3] = {n1, n2, n3};
    vector<int> ordenado = {n1, n2, n3};

    // Ordenando
    sort(ordenado.begin(), ordenado.end());

    for(int cont = 0; cont < 3; cont++){
        cout << ordenado[cont] << endl;
    }

    printf("\n");

    for(int cont = 0; cont < 3; cont++){
        cout << lista[cont] << endl;
    }

    return 0;
}