// Caio Cesar 29/11/23
// BEE 1174

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float num;
    int i;

    for(i = 0; i < 100; i++){
        cin >> num;
        if(num <= 10){
            cout << "A[" << i << "] = " << fixed << setprecision(1) << num << endl;
        }
    }

    return 0;
}