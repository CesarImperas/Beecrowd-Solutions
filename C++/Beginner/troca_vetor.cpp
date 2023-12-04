// Caio Cesar 30/11/23
// BEE 1072

#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> vetor;
    int num;

    for(int i = 0; i < 20; i++){
        cin >> num;
        vetor.push_back(num);
    }

    int indice = 0;
    for(auto it = vetor.rbegin(); it != vetor.rend(); it++){
        cout << "N[" << indice << "] = " << *it << endl;
        indice++;
    }

    return 0;
}