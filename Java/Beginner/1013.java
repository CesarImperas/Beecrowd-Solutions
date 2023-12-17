import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int a, b, c, maiorAB;

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        maiorAB = (int) (a + b + Math.abs(a-b)) / 2;

        if(maiorAB > c){
            System.out.println(maiorAB + " eh o maior");
        }else{
            System.out.println(c + " eh o maior");
        }

    }
}
