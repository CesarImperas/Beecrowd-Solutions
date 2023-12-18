import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        
        int num, i;

        for(i = 0; i < 10; i++){
            num = sc.nextInt();

            if(num <= 0){
                num = 1;
            }

            System.out.printf("X[%d] = %d\n", i, num);
        }

    
        sc.close();
    }
}