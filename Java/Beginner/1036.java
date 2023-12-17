import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double numA, numB, numC, delta, x1, x2;

        numA = sc.nextDouble();
        numB = sc.nextDouble();
        numC = sc.nextDouble();


        delta = Math.pow(numB, 2) - (4 * numA * numC);

        if(delta < 0 || numA == 0){
            System.out.printf("Impossivel calcular\n");
        }else{
            x1 = ((- numB) + Math.sqrt(delta)) / (2.0 * numA);
            x2 = ((- numB) - Math.sqrt(delta)) / (2.0 * numA);

            System.out.printf("R1 = %.5f\n", x1);
            System.out.printf("R2 = %.5f\n", x2);
        }

        sc.close();
    }
}