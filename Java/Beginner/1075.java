import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n;

        n = sc.nextInt();

        for(int i=2; i<10000; i++){
            if(i % n == 2){
                System.out.println(i);
            }
        }
        
        sc.close();
    }
}