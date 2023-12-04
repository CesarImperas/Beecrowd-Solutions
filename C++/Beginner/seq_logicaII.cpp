// Caio Cesar 02/12/23
// BEE 1145

#include <iostream>
using namespace std;

int main(){
    int valor_x, valor_y, x = 1, y;

    cin >> valor_x >> valor_y;

    for(y = 1; y < valor_y + 1; y++){
        if(x == valor_x){
            cout << y << endl;
            x = 1;
        }else{
            cout << y << " ";
            x++;
        }
    }
}