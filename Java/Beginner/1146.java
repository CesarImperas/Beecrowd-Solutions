import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int x;
        String number = "";

        while(true){
            x = sc.nextInt();

            if(x == 0) break;

            for(int num=1; num<(x+1); num++){
                if(num == x){
                    number += num;
                }else{
                    number += num;
                    number += " ";
                }
            }

            System.out.println(number);

            number = "";
        }

        sc.close();
    }
}
