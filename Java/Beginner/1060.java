import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int positivos = 0;
        float numeros;

        for(int cont=0; cont<6; cont++){
            numeros = sc.nextFloat();
            if(numeros > 0){
                positivos++;
            }
        }

        System.out.printf("%d valores positivos\n", positivos);

        sc.close();
    
    }
}
