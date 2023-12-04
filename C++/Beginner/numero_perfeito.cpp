// Caio Cesar 02/12/23
// BEE 1164

#include <iostream>
using namespace std;

int main(){
    int casos, num, soma, n;

    cin >> casos;

    for(int i = 0; i < casos; i++){
        cin >> num;
        soma = 0;
        for(n = 1; n < num; n++){
            if((n % num == 0) || (num % n == 0)){
                soma += n;
            }
        }

        if(soma == num){
            cout << num << " eh perfeito" << endl;
        }else{
            cout << num << " nao eh perfeito" << endl;
        }
    }

    return 0;
}