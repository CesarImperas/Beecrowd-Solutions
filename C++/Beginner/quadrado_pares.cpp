// Caio Cesar 01/12/23
// BEE 1073

#include <iostream>
using namespace std;

int main(){
    int numero;

    cin >> numero;

    for(int quad = 2; quad < numero + 1; quad += 2){
        cout << quad << "^2 = " << quad*quad << endl;
    }

    return 0;
}