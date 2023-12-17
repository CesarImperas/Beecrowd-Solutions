import java.util.Scanner;
import java.util.Locale;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int tempo, velocidaMedia;
        double litros;

        tempo = sc.nextInt();
        velocidaMedia = sc.nextInt();
    

        litros = (tempo * velocidaMedia)/12.0;

        System.out.printf("%.3f\n", litros);

        sc.close();
    }
}