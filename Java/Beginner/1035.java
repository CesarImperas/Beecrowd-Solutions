import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int a, b, c, d, somacd, somaab;

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();

        somacd = c + d;
        somaab = a + b;

        if((b > c) && (d > a) && (somacd > somaab) && (c >= 0 && d >= 0) && (a % 2 == 0)){
            System.out.printf("Valores aceitos\n");
        }else{
            System.out.printf("Valores nao aceitos\n");
        }

        sc.close();

    }
}