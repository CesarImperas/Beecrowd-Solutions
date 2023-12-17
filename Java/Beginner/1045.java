import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        float[] vect = new float[3];
        float A, B, C, aux;

        vect[0] = sc.nextFloat();
        vect[1] = sc.nextFloat();
        vect[2] = sc.nextFloat();

        for (int i = 0; i < vect.length; i++){
            for(int j = 0; j < vect.length; j++) {
                if(vect[i] > vect[j]) {

                    aux = vect[i];
                    vect[i] = vect[j];
                    vect[j] = aux;
                }

            }  
        }

        A = vect[0];
        B = vect[1];
        C = vect[2];

    
        if(A >= B + C){
            System.out.println("NAO FORMA TRIANGULO");
        }else if((A*A) == (B*B) + (C*C)){
            System.out.println("TRIANGULO RETANGULO");
        }else if((A*A) > (B*B) + (C*C)){
            System.out.println("TRIANGULO OBTUSANGULO");
        }else if((A*A) < (B*B) + (C*C)){
            System.out.println("TRIANGULO ACUTANGULO");
        }
    
        if((A == B) && (B == C) && (A == C)){
            System.out.println("TRIANGULO EQUILATERO");
        }else if((A == B) || (B == C)){
            System.out.println("TRIANGULO ISOSCELES");
        } 

        sc.close();
    }
}