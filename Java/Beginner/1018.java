import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int dinheiro, nota100, nota50, nota20, nota10, nota5, nota2, nota1;

        dinheiro = sc.nextInt();

        System.out.println(dinheiro);

        nota100 = dinheiro / 100;
        dinheiro = dinheiro % 100;

        nota50 = dinheiro / 50;
        dinheiro = dinheiro % 50;

        nota20 = dinheiro / 20;
        dinheiro = dinheiro % 20;

        nota10 = dinheiro / 10;
        dinheiro = dinheiro % 10;

        nota5 = dinheiro / 5;
        dinheiro = dinheiro % 5;

        nota2 = dinheiro / 2;
        dinheiro = dinheiro % 2;

        nota1 = dinheiro;
        
        System.out.printf("%d nota(s) de R$ 100,00\n", nota100);
        System.out.printf("%d nota(s) de R$ 50,00\n", nota50);
        System.out.printf("%d nota(s) de R$ 20,00\n", nota20);
        System.out.printf("%d nota(s) de R$ 10,00\n", nota10);
        System.out.printf("%d nota(s) de R$ 5,00\n", nota5);
        System.out.printf("%d nota(s) de R$ 2,00\n", nota2);
        System.out.printf("%d nota(s) de R$ 1,00\n", nota1);

        sc.close();

    }
}