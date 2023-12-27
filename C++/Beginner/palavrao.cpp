// Caio Cesar 25/12/23
// BEE 3303

#include <iostream>
#include <cstring>
using namespace std;

int main(){
    string palavra;

    cin >> palavra;

    if(palavra.size() >= 10){
        cout << "palavrao" << endl;
    }else{
        cout << "palavrinha" << endl;
    }

    return 0;
}
