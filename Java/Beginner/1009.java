import java.util.Scanner;
import java.io.IOException;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String nome;
        double salario_fixo, vendas, salario_bonus;

        nome = sc.nextLine();
        salario_fixo = sc.nextDouble();
        vendas = sc.nextDouble();

        salario_bonus = (double) (vendas * 0.15) + salario_fixo;

        System.out.printf("TOTAL = R$ %.2f\n", salario_bonus);
        
        sc.close();

    }
}