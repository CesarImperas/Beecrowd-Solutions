// Caio Cesar 01/12/23
// BEE 1158

#include <iostream>
using namespace std;

int main(){
    int casos, num, qntd, soma;

    cin >> casos;

    for(int i = 0; i < casos; i++){
        cin >> num >> qntd;

        soma = 0;
        while(qntd > 0){
            if(num % 2 != 0){
                soma += num;
                qntd--;
            }
            num++;
        }

        cout << soma << endl;
    }

    return 0;
}
