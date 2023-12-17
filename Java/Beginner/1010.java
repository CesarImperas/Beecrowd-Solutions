import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int cod1, num1, cod2, num2;
        float valor1, valor2, calculo;

        cod1 = sc.nextInt();
        num1 = sc.nextInt();
        valor1 = sc.nextFloat();

        cod2 = sc.nextInt();
        num2 = sc.nextInt();
        valor2 = sc.nextFloat();

        calculo = (num1 * valor1) + (num2 * valor2);

        System.out.printf("VALOR A PAGAR: R$ %.2f\n", calculo);

        
        sc.close();
    }
}