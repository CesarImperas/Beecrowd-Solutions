import java.util.Scanner;
import java.io.IOException;
import java.util.Locale;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        float num;

        num = sc.nextFloat();

        if(num >= 0 && num <= 25){
            System.out.printf("Intervalo [0,25]\n");
        }else if(num > 25 && num <= 50){
            System.out.printf("Intervalo (25,50]\n");
        }else if(num > 50 && num <= 75){
            System.out.printf("Intervalo (50,75]\n");
        }else if(num > 75 && num <= 100){
            System.out.printf("Intervalo (75,100]\n");
        }else{
            System.out.printf("Fora de intervalo\n");
        }
    }
}
