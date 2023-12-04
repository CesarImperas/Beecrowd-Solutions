// Caio Cesar 01/12/23
// BEE 1113

#include <iostream>
using namespace std;

int main(){
    int num_x, num_y;
    do{
        cin >> num_x >> num_y;

        if(num_x > num_y){
            cout << "Decrescente" << endl;
        }else if(num_x < num_y){
            cout << "Crescente" << endl;
        }

    } while(num_x != num_y);

    return 0;
}