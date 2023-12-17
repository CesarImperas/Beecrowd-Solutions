import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int x, y, maior, menor;

        x = sc.nextInt();
        y = sc.nextInt();

        if(x>y){
            maior = x;
            menor = y;
        }else{
            maior = y;
            menor = x;
        }

        for(int num=(menor+1); num<maior; num++){
            if(num % 5 == 2 || num % 5 == 3){
                System.out.println(num);
            }
        }

        sc.close();
    }
}
