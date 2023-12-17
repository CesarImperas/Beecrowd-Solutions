import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double n1, n2, n3, n4, n5, media_pon, media_nova;

        n1 = sc.nextDouble();
        n2 = sc.nextDouble();
        n3 = sc.nextDouble();
        n4 = sc.nextDouble();

        media_pon = ((n1*2.0)+(n2*3.0)+(n3*4.0)+(n4*1.0)) / 10.0;

        System.out.printf("Media: %.1f\n", media_pon - 0.0001);

        if(media_pon >= 7.0){
            System.out.printf("Aluno aprovado.\n");
        }else if(media_pon < 5.0){
            System.out.printf("Aluno reprovado.\n");
        }else{
            System.out.printf("Aluno em exame.\n");
            n5 = sc.nextDouble();

            System.out.printf("Nota do exame: %.1f\n", n5);

            media_nova = (n5 + media_pon) / 2.0;

            if(media_nova >= 5){
                System.out.printf("Aluno aprovado.\n");
                System.out.printf("Media final: %.1f\n", media_nova);
            }else{
                System.out.printf("Aluno reprovado.\n");
                System.out.printf("Media final: %.1f\n", media_nova);
            }
        }

        sc.close();
    }
}