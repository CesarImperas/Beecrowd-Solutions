import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int linhas, n1, n2, n3;
        String pum = "";

        linhas = sc.nextInt();

        n1 = 1;
        n2 = 2;
        n3 = 3;

        for(int i=0; i<linhas; i++){
            pum += n1 + " " + n2 + " " + n3 + " PUM\n";
            
            n1 += 4;
            n2 += 4;
            n3 += 4;
        }

        System.out.print(pum);

        sc.close();
    }
}
