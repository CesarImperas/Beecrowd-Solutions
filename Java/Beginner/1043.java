import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        float n1, n2, n3, perimetro, area;

        n1 = sc.nextFloat();
        n2 = sc.nextFloat();
        n3 = sc.nextFloat();

        if((n1 + n2 > n3) && (n1 + n3 > n2) && (n2 + n3 > n1)){
            perimetro = n1 + n2 + n3;
            System.out.printf("Perimetro = %.1f\n", perimetro);
        }else{
            area = ((n1 + n2) * n3)/2;
            System.out.printf("Area = %.1f\n", area);
        }
        sc.close();
    }
}