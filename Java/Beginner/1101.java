import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int M, N, maior, menor, soma;
        String numeros;

        while(true){
            
            M = sc.nextInt();
            N = sc.nextInt();

            if(M <= 0 || N <= 0) break;

            maior = 0;
            menor = 0;
            
            numeros = "";
            soma = 0;

            if(M > N){
                maior += M;
                menor += N;
            }else if(N > M){
                maior += N;
                menor += M;
            }else{
                maior += M;
                menor += N;
            }

            for(int j=menor; j<(maior+1); j++){
                numeros += j + " ";
                soma += j;
            }
            

            System.out.printf("%sSum=%d\n", numeros, soma);
        }

        sc.close();
    }
}
