// Caio Cesar 24/12/23
// BEE 1155

#include <cstdio>
using namespace std;

int main(){
    double soma = 0;

    for(int i = 1;i <= 100; i++){
        soma += ((double) 1 / i); 
    }

    printf("%.2lf\n", soma);

    return 0;
}