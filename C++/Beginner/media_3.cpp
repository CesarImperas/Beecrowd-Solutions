// Caio Cesar 29/11/23
// BEE 1040

#include <cstdio>

int main(){
    float n1, n2, n3, n4, n5, media_pon, media_nova;

    scanf("%f %f %f %f", &n1, &n2, &n3, &n4);

    media_pon = ((n1*2.0)+(n2*3.0)+(n3*4.0)+(n4*1.0)) / 10.0;

    printf("Media: %.1f\n", media_pon);

    if(media_pon >= 7.0){
        printf("Aluno aprovado.\n");
    }else if(media_pon < 5.0){
        printf("Aluno reprovado.\n");
    }else{
        printf("Aluno em exame.\n");
        scanf("%f", &n5);

        printf("Nota do exame: %.1f\n", n5);

        media_nova = (n5 + media_pon) / 2.0;

        if(media_nova >= 5){
            printf("Aluno aprovado.\n");
            printf("Media final: %.1f\n", media_nova);
        }else{
            printf("Aluno reprovado.\n");
            printf("Media final: %.1f\n", media_nova);
        }
    }

    return 0;
}