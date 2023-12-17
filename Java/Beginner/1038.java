import java.util.Locale;
import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int cod, qntd;
        double valor;

        cod = sc.nextInt();
        qntd = sc.nextInt();

        if(cod == 1){
            valor = qntd * 4.0;
        }else if(cod == 2){
            valor = qntd * 4.5;
        }else if(cod == 3){
            valor = qntd * 5.0;
        }else if(cod == 4){
            valor = qntd * 2.0;
        }else{
            valor = qntd * 1.5;
        }

        System.out.printf("Total: R$ %.2f\n", valor);

        sc.close();
    }
}
