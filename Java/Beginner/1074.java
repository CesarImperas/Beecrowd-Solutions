import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int teste, num;

        teste = sc.nextInt();

        for(int cont = 0; cont < teste; cont++){
            num = sc.nextInt();

            if(num == 0){
                System.out.println("NULL");
            }else if(num < 0 && num % 2 == 0){
                System.out.println("EVEN NEGATIVE");
            }else if(num < 0 && num % 2 != 0){
                System.out.println("ODD NEGATIVE");
            }else if(num > 0 && num % 2 == 0){
                System.out.println("EVEN POSITIVE");
            }else if(num > 0 && num % 2 != 0){
                System.out.println("ODD POSITIVE");
            }
        }

        sc.close();
    }
}