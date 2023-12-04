// Caio Cesar 30/11/23
// BEE 1066

#include <iostream>

int main(){
    int pares = 0, impares = 0, positivos = 0, negativos = 0;
    int num;

    for(int i = 0; i < 5; i++){
        std::cin >> num;
        if(num % 2 == 0){
            pares += 1;
        }else{
            impares += 1;
        }
        
        if(num > 0){
            positivos += 1;
        }else if(num < 0){
            negativos += 1;
        }
    }

    std::cout << pares << " valor(es) par(es)" << std::endl;
    std::cout << impares << " valor(es) impar(es)" << std::endl;
    std::cout << positivos << " valor(es) positivo(s)" << std::endl;
    std::cout << negativos << " valor(es) negativo(s)" << std::endl;

    return 0;
}