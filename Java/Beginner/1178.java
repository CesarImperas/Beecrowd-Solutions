import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double[] vect = new double[100];

        double n = sc.nextDouble();

        for(int i=0; i<vect.length; i++){
            System.out.printf("N[%d] = %.4f\n", i, n);
            n /= 2.0;
        }

        sc.close();
    }
}