import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        float x, y;
        String resposta = null;

        x = sc.nextFloat();
        y = sc.nextFloat();

        if(x == 0 && y == 0){
            resposta = "Origem";
        }else if((x == 0 && y > 0) || (x == 0 && y < 0)){
            resposta = "Eixo Y";
        }else if((x > 0 && y == 0) || (x < 0 && y == 0)){
            resposta = "Eixo X";
        }else if(x > 0 && y > 0){
            resposta = "Q1";
        }else if(x < 0 && y > 0){
            resposta = "Q2";
        }else if(x < 0 && y < 0){
            resposta = "Q3";
        }else if(x > 0 && y < 0){
            resposta = "Q4";
        }

        System.out.println(resposta);

        sc.close();

    }
}
