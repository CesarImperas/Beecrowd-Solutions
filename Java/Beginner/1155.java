import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int denominador = 1;
        double soma = 0;

        while(denominador <= 100){
            soma += 1.0/denominador;
            denominador += 1;
        }

        System.out.printf("%.2f\n", soma);

        sc.close();
    }
}