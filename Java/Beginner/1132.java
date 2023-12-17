import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int num_x, num_y, soma = 0, n;

        num_x = sc.nextInt();
        num_y = sc.nextInt();
        
        if(num_x > num_y){
            for(n = num_y; n < num_x + 1; n++){
                if(n % 13 != 0){
                    soma += n;
                }
            }
        }else if(num_y > num_x){
            for(n = num_x; n < num_y + 1; n++){
                if(n % 13 != 0){
                    soma += n;
                }
            }
        }

        System.out.println(soma);

        sc.close();
    }
}
