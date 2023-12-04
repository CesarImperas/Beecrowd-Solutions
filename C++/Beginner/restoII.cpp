// Caio Cesar 30/11/23
// BEE 1075

#include <iostream>
using namespace std;

int main(){
    int valor, num;

    cin >> valor;
    
    for(num = 2; num < 10000; num++){
        if(num % valor == 2){
            cout << num << endl;
        }
    }

    return 0;
}