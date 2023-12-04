// Caio Cesar 30/11/23
// BEE 1050

#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
    map<int, string> ddd = {{61, "Brasilia"}, {71, "Salvador"}, {11, "Sao Paulo"}, {21, "Rio de Janeiro"}, {32, "Juiz de Fora"}, {19, "Campinas"}, {27, "Vitoria"}, {31, "Belo Horizonte"}};
    int num;
    bool existe = false;

    cin >> num;

    map<int, string>::iterator i;
    for(i = ddd.begin(); i != ddd.end(); i++){
        if((*i).first == num){
            existe = true;
            cout << i->second << endl;
        }
    }

    if(!existe){
        cout << "DDD nao cadastrado" << endl;
    }

    return 0;

}