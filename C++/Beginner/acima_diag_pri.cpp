// Caio Cesar 11/12/23
// BEE 1185

#include <iostream>
using namespace std;

int main(){
    double mat[12][12];
    int linha, coluna, qntd = 0;
    double soma = 0, media;
    char operacao;

    
    cin >> operacao;

    for(linha = 0; linha < 12; linha++){
        for(coluna = 0; coluna < 12; coluna++){
            cin >> mat[linha][coluna];
            if(coluna < 11 - linha){
                soma += mat[linha][coluna];
                qntd++;
            }
        }
    }

    if(operacao == 'S'){
        printf("%.1lf\n", soma);
    }else{
        media = soma / qntd;
        printf("%.1lf\n", media);
    }

    return 0;
}
