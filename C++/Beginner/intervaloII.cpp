// Caio Cesar 30/11/23
// BEE 1072

#include <iostream>
using namespace std;

int main(){
    int cont, dentro = 0, fora = 0;
    int num;

    cin >> cont;

    while(cont){
        cont--;
        cin >> num;
        if(num >= 10 && num <= 20){
            dentro++;
        }else{
            fora++;
        }
    }

    cout << dentro << " in" << endl;
    cout << fora << " out" << endl;

    return 0;
}