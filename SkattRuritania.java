//  OPPGAVE 01.04

import java.util.Scanner;

public class SkattRuritania {
    public static void main(String[] args){
        System.out.println("Tast inn din inntekt:");
        Scanner input = new Scanner(System.in);
        double inntekt = input.nextInt();
        double skatt = 0;
        if (inntekt < 10000){
            skatt = inntekt * 0.1;
        } else if (inntekt >= 10000) {
            skatt = ((10000 * 0.1) + (inntekt - 10000) * 0.3);
        }
        System.out.println("Du betaler "+ skatt + "kr i skatt.");
    }
}
