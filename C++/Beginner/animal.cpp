// Caio Cesar 01/12/23
// BEE 1049

#include <iostream>
#include <string>
using namespace std;

int main(){
    string coluna, classe, alimento;

    cin >> coluna;
    cin >> classe;
    cin >> alimento;

    if(coluna == "vertebrado"){
        if(classe == "ave"){
            if(alimento == "carnivoro"){
                cout << "aguia" << endl;
            }else{
                cout << "pomba" << endl;
            }
        }else{
            if(alimento == "onivoro"){
                cout << "homem" << endl;
            }else{
                cout << "vaca" << endl;
            }
        }
    }else{
        if(classe == "inseto"){
            if(alimento == "hematofago"){
                cout << "pulga" << endl;
            }else{
                cout << "lagarta" << endl;
            }
        }else{
            if(alimento == "hematofago"){
                cout << "sanguessuga" << endl;
            }else{
                cout << "minhoca" << endl;
            }
        }
    }

    return 0;
}