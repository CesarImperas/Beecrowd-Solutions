// Caio Cesar 11/12/23
// BEE 1184

#include <iostream>
using namespace std;

int main(){
    double mat[12][12];
    int linha, coluna;
    double soma = 0, media;
    char operacao;

    cin >> operacao;

    for(linha = 0; linha < 12; linha++){
        for(coluna = 0; coluna < 12; coluna++){
            cin >> mat[linha][coluna];
            if(linha > coluna){
                soma += mat[linha][coluna];
            }
        }
    }

    if(operacao == 'S'){
        printf("%.1lf\n", soma);
    }else{
        media = soma / 66.0;
        printf("%.1lf\n", media);
    }

    return 0;
}
