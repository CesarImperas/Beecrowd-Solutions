import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int contador = 0;
        double soma = 0, nota, media;

        while(contador < 2){
            nota = sc.nextDouble();

            if(nota >= 0 && nota <= 10){
                soma += nota;
                contador++;
            }else{
                System.out.println("nota invalida");
            }
        }

        media = soma / 2.0;

        System.out.printf("media = %.2f\n", media);

        sc.close();
    }
}