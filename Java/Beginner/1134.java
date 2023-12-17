import java.util.Scanner;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        
        int entrada, alcool = 0, diesel = 0, gasolina = 0;

        while(true){
            entrada = sc.nextInt();

            if(entrada == 1){
                alcool += 1;
            }else if(entrada == 2){
                gasolina += 1;
            }else if(entrada == 3){
                diesel += 1;
            }else if(entrada == 4) break;
        }

        System.out.println("MUITO OBRIGADO");
        System.out.println("Alcool: " + alcool);
        System.out.println("Gasolina: " + gasolina);
        System.out.println("Diesel: " + diesel);
        
        sc.close();
    }
}