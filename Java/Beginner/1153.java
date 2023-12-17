import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int num, fatorial;

        num = sc.nextInt();

        fatorial = 1;
        for(int i = 1; i <= num; i++){
            fatorial *= i;
        }

        System.out.println(fatorial);

        sc.close();

    }    
}
