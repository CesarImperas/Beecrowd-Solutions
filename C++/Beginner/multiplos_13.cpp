// Caio Cesar 01/12/23
// BEE 1113

#include <iostream>
using namespace std;

int main(){
    int num_x, num_y, soma = 0, n;

    cin >> num_x;
    cin >> num_y;
    
    if(num_x > num_y){
        for(n = num_y; n < num_x + 1; n++){
            if(n % 13 != 0){
                soma += n;
            }
        }
    }else if(num_y > num_x){
        for(n = num_x; n < num_y + 1; n++){
            if(n % 13 != 0){
                soma += n;
            }
        }
    }

    cout << soma << endl;

    return 0;
}