import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double f1, f2, flutuacao;

        f1 = sc.nextDouble();
        f2 = sc.nextDouble();

        flutuacao = (((1 + (f1/100.0)) * (1 + (f2/100.0))) - 1) * 100.0;

        System.out.printf("%.6f\n", flutuacao);

        sc.close();
    }
}
