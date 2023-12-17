import java.util.Scanner;
import java.util.Locale;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int distancia;
        float combustivel, consumo;

        distancia = sc.nextInt();
        combustivel = sc.nextFloat();

        consumo = distancia/combustivel;

        System.out.printf("%.3f km/l\n", consumo);


        sc.close();
    }
}