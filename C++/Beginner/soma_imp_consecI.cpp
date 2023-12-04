// Caio Cesar 30/11/23
// BEE 1071

#include <iostream>
using namespace std;

int main(){
    int soma = 0, num_x, num_y;

    cin >> num_x;
    cin >> num_y;

    for(int cont = num_y + 1; cont < num_x; cont++){
        if(cont % 2 != 0){
            soma += cont;
        }
    }

    cout << soma << endl;

    return 0;
}