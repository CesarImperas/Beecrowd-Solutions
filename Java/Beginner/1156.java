import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int numerador = 1, denominador = 1;
        double soma = 0;

        while(numerador <= 39){
            soma += ((double) numerador/(double) denominador);
            numerador += 2;
            denominador *= 2;
        }

        System.out.printf("%.2f\n", soma);
        
        sc.close();
    }
}