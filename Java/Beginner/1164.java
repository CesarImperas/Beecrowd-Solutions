import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int casos, num, soma, n;

        casos = sc.nextInt();

        for(int i = 0; i < casos; i++){
            num = sc.nextInt();
            soma = 0;
            for(n = 1; n < num; n++){
                if((n % num == 0) || (num % n == 0)){
                    soma += n;
                }
            }

            if(soma == num){
                System.out.print(num + " eh perfeito\n");
            }else{
                System.out.print(num + " nao eh perfeito\n");
            }
        }
        
        sc.close();
    }
}