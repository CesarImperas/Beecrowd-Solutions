import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        
        int inicio;

        inicio = sc.nextInt();

        for(int i=0; i<10; i++){
            System.out.printf("N[%d] = %d\n", i, inicio);
            inicio *= 2;
        }
        
        sc.close();
    }
}