import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int hrI, hrF, tempo;

        hrI = sc.nextInt();
        hrF = sc.nextInt();

        if(hrI >= hrF){
            tempo = 24 - hrI + hrF;
        }else{
            tempo = hrF - hrI;
        }

        System.out.println("O JOGO DUROU " + tempo + " HORA(S)");
        
        sc.close();

    }
}
