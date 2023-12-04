// Caio Cesar 29/11/23
// BEE 1172

#include <iostream>
using namespace std;

int main(){
    int num, i;

    for(i = 0; i < 10; i++){
        cin >> num;
        if(num <= 0){
            num = 1;
        }

        cout << "X[" << i << "] = " << num << endl;
    }

    return 0;
}