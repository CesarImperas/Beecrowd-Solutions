import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        List<Integer> lista = new ArrayList<>();

        lista.add(0);
        lista.add(1);

        int n = sc.nextInt();

        int valor1, valor2;
        int indice1 = 0, indice2 = 1;

        while(lista.size() < n){
            valor1 = lista.get(indice1);
            valor2 = lista.get(indice2);
            lista.add(valor1 + valor2);
            indice1++;
            indice2++;
        }

        for(int i=0; i<n; i++){
            if(i == n-1){
                System.out.println(lista.get(i));
            }else{
                System.out.print(lista.get(i) + " ");
            }
        }

        sc.close();
    }
}