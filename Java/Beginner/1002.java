import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double raio, area;

        raio = sc.nextDouble();

        area = 3.14159 * Math.pow(raio, 2);
       
        System.out.printf("A=%.4f\n", area);

        sc.close();

    }

}