import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double[][] mat = new double[12][12];

        int linhaUser;
        double soma = 0, media;
        char operacao;

        linhaUser = sc.nextInt();
        operacao = sc.next().charAt(0);

        for(int linha=0; linha<12; linha++){
            for(int coluna =0; coluna<12; coluna++){
                mat[linha][coluna] = sc.nextDouble();
                if(linha == linhaUser){
                    soma += mat[linha][coluna];
                }
            }
        }

        if(operacao == 'M'){
            media = soma / 12.0;
            System.out.printf("%.1f\n", media);
        }else{
            System.out.printf("%.1f\n", soma);
        }


        sc.close();
    }
}