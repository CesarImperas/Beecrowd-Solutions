import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        
        int x, y;

        while(true){
            x = sc.nextInt();
            y = sc.nextInt();

            if(x == 0 || y == 0) break;

            if(x > 0 && y > 0){
                System.out.println("primeiro");
            }else if(x < 0 && y > 0){
                System.out.println("segundo");
            }else if(x < 0 && y < 0){
                System.out.println("terceiro");
            }else if(x > 0 && y < 0){
                System.out.println("quarto");
            }
        }

        sc.close();
    }
}