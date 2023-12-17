import java.util.Scanner;
import java.io.IOException;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int casos;
        float num1, num2, div;

        casos = sc.nextInt();

        for(int i = 0; i < casos; i++){
            num1 = sc.nextFloat();
            num2 = sc.nextFloat();

            if(num2 == 0){
                System.out.println("divisao impossivel");
            }else{
                div = (float) (num1 / num2);
                System.out.printf("%.1f\n", div);
            }
        }

        sc.close();

    }    
}
