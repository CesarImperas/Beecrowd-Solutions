// Caio Cesar 30/11/23
// BEE 1074

#include <iostream>
using namespace std;

int main(){
    int teste, num;

    cin >> teste;

    for(int cont = 0; cont < teste; cont++){
        cin >> num;
        if(num == 0){
            cout << "NULL" << endl;
        }else if(num < 0 && num % 2 == 0){
            cout << "EVEN NEGATIVE" << endl;
        }else if(num < 0 && num % 2 != 0){
            cout << "ODD NEGATIVE" << endl;
        }else if(num > 0 && num % 2 == 0){
            cout << "EVEN POSITIVE" << endl;
        }else if(num > 0 && num % 2 != 0){
            cout << "ODD POSITIVE" << endl;
        }
    }

    return 0;
}