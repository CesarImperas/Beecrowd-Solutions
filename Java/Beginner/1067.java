import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int num;

        num = sc.nextInt();
        
        for(int i = 1; i <= num; i += 1){
            if(i % 2 != 0){
                System.out.println(i);
            }
        }

        sc.close();
    }
}