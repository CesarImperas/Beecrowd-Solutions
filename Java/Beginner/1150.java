import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        
        int x, y, soma = 0, cont = 0;

        x = sc.nextInt();
        y = sc.nextInt();

        while(x >= y){
            y = sc.nextInt();
        }

        while(soma < y){
            soma += x;
            x += 1;
            cont += 1;
        }

        System.out.println(cont);

        sc.close();
    }
}