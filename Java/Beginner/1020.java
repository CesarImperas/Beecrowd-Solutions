import java.util.Scanner;
import java.util.Locale;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int dias, aux, meses, anos;
        
        dias = sc.nextInt();

        aux = dias % 365;
        anos = dias / 365;
        meses = aux / 30;
        dias = aux % 30;

        System.out.printf("%d ano(s)\n", anos);
        System.out.printf("%d mes(es)\n", meses);
        System.out.printf("%d dia(s)\n", dias);

        sc.close();
    }
}