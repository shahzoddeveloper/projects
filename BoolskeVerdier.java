//OPPGAVE 01.07

public class BoolskeVerdier {
    public static void main(String[] args){
        boolean sann = true;
        boolean usann = false;
        System.out.println(sann);
        System.out.println(usann);

        if (sann != usann) {
            System.out.println("Forste test slo til!");
        } else {
            System.out.println("Noe gikk feil");
        }

        if (sann == usann) {
            System.out.println("Noe gikk feil");
        } else {
            System.out.println("Andre test slo ikke til!");
        }
    }
}
