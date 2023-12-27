import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int[] vect = new int[1000];

        int n = sc.nextInt();

        int contador = 0;
        for(int i=0; i<1000; i++){
            System.out.println("N[" + i + "] = " + contador);

            contador++;

            if(contador == n){
                contador = 0;
            }
        }
        
        sc.close();
    }
}