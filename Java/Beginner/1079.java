import java.util.Scanner;
import java.io.IOException;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int cont;
        float num1, num2, num3, media;
    
        cont = sc.nextInt();
        
        for(int i = 0; i < cont; i += 1){
            num1 = sc.nextFloat();
            num2 = sc.nextFloat();
            num3 = sc.nextFloat();

            media = (float) ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10;

            System.out.printf("%.1f\n", media);
        }

        sc.close();
    }
}