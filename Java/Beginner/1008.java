import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int num, hora;
        float valor, salario;

        num = sc.nextInt();
        hora = sc.nextInt();
        valor = sc.nextFloat();

        salario = hora * valor;

        System.out.println("NUMBER = " + num);
        System.out.printf("SALARY = U$ %.2f\n", salario);
        
        sc.close();
    }
}