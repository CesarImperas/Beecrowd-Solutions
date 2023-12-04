// Caio Cesar 29/11/23
// BEE 1159

#include <iostream>
using namespace std;

int main(){
    int num, soma, cont;

    while(true){
        cin >> num;
        if(num == 0) break;

        soma = 0;
        cont = 0;
        while(cont < 5){
            if(num % 2 == 0){
                soma += num;
                cont++;
            }
            num++;
        }

        cout << soma << endl;
    }

    return 0;
}