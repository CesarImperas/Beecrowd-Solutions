// Caio Cesar 01/12/23
// BEE 1113

#include <iostream>
using namespace std;

int main(){
    int casos, num_x, num_y, soma;
    int i, n;

    cin >> casos;

    for(i = 0; i < casos; i++){
        cin >> num_x >> num_y;

        soma = 0;
        if(num_x > num_y){
            for(n = num_y + 1; n < num_x; n++){
                if(n % 2 != 0){
                    soma += n;
                }
            }
        }else if(num_y > num_x){
            for(n = num_x + 1; n < num_y; n++){
                if(n % 2 != 0){
                    soma += n;
                }
            }
        }

        cout << soma << endl;
    }

    return 0;
}